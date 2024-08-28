# Start by importing some things we will need
import numpy as np
from math import floor, sqrt
from scipy.ndimage import gaussian_filter
from scipy.stats import multivariate_normal


# Now let's define the prior function. In this case, we choose
# to initialize the histogram based on a Gaussian distribution around [0,0]
def histogram_prior(belief, grid_spec, mean_0, cov_0):
    pos = np.empty(belief.shape + (2,))
    pos[:, :, 0] = grid_spec["d"]
    pos[:, :, 1] = grid_spec["phi"]
    RV = multivariate_normal(mean_0, cov_0)
    belief = RV.pdf(pos)
    return belief


# Now let's define the predict function
def histogram_predict(belief, left_encoder_ticks, right_encoder_ticks, grid_spec, robot_spec, cov_mask):
    belief_in = belief

    # Calculate v (linear velocity) and w (angular velocity)
    wheel_base = robot_spec['wheel_base']
    ticks_to_distance = robot_spec['ticks_to_distance']

    v = (left_encoder_ticks + right_encoder_ticks) * ticks_to_distance / 2.0
    w = (right_encoder_ticks - left_encoder_ticks) * ticks_to_distance / wheel_base

    maxids = np.unravel_index(belief_in.argmax(), belief_in.shape)
    phi_max = grid_spec['phi_min'] + (maxids[1] + 0.5) * grid_spec['delta_phi']

    # Propagate each centroid
    d_t = grid_spec["d"] + v
    phi_t = grid_spec["phi"] + w

    p_belief = np.zeros(belief.shape)

    for i in range(belief.shape[0]):
        for j in range(belief.shape[1]):
            if belief[i, j] > 0:
                if (
                    d_t[i, j] > grid_spec["d_max"]
                    or d_t[i, j] < grid_spec["d_min"]
                    or phi_t[i, j] < grid_spec["phi_min"]
                    or phi_t[i, j] > grid_spec["phi_max"]
                ):
                    continue

                # Calculate the new indices based on the updated positions
                i_new = int((d_t[i, j] - grid_spec["d_min"]) / grid_spec["delta_d"])
                j_new = int((phi_t[i, j] - grid_spec["phi_min"]) / grid_spec["delta_phi"])

                if 0 <= i_new < belief.shape[0] and 0 <= j_new < belief.shape[1]:
                    p_belief[i_new, j_new] += belief[i, j]

    # Add noise according to the process model noise
    s_belief = np.zeros(belief.shape)
    gaussian_filter(p_belief, cov_mask, output=s_belief, mode="constant")

    if np.sum(s_belief) == 0:
        return belief_in

    belief = s_belief / np.sum(s_belief)
    return belief


# Function to filter segments based on their color and position
def prepare_segments(segments, grid_spec):
    filtered_segments = []
    for segment in segments:
        # Update to filter out colors that are not the specific RGBA for left and right
        if (segment.color != (131, 121, 108, 255) and segment.color != (38, 37, 46, 255)):
            continue

        # Filter out any segments that are behind the robot
        if segment.points[0].x < 0 or segment.points[1].x < 0:
            continue

        point_range = getSegmentDistance(segment)
        if grid_spec["range_est"] > point_range > 0:
            filtered_segments.append(segment)
    return filtered_segments


# Function to generate votes for lane positions based on segment color and position
def generate_vote(segment, road_spec):
    p1 = np.array([segment.points[0].x, segment.points[0].y])
    p2 = np.array([segment.points[1].x, segment.points[1].y])
    t_hat = (p2 - p1) / np.linalg.norm(p2 - p1)
    n_hat = np.array([-t_hat[1], t_hat[0]])

    d1 = np.inner(n_hat, p1)
    d2 = np.inner(n_hat, p2)
    l1 = np.inner(t_hat, p1)
    l2 = np.inner(t_hat, p2)
    if l1 < 0:
        l1 = -l1
    if l2 < 0:
        l2 = -l2

    l_i = (l1 + l2) / 2
    d_i = (d1 + d2) / 2
    phi_i = np.arcsin(t_hat[1])

    # Update the logic to check for specific RGBA values for left and right lanes
    if segment.color == (131, 121, 108, 255):  # Left lane is off-white (rgba(131,121,108,255))
        if p1[0] > p2[0]:  # left edge of the left lane
            d_i -= road_spec["linewidth_off_white"]
        else:  # right edge of the left lane
            d_i -= road_spec["linewidth_off_white"]
            d_i = road_spec["lanewidth"] * 2 + road_spec["linewidth_black"] - d_i
            phi_i = -phi_i
        d_i -= road_spec["lanewidth"] / 2

    elif segment.color == (38, 37, 46, 255):  # Right lane is black (rgba(38,37,46,255))
        if p2[0] > p1[0]:  # left edge of the right lane
            d_i -= road_spec["linewidth_black"]
            d_i = road_spec["lanewidth"] / 2 - d_i
            phi_i = -phi_i
        else:  # right edge of the right lane
            d_i += road_spec["linewidth_black"]
            d_i -= road_spec["lanewidth"] / 2

    return d_i, phi_i


# Function to generate measurement likelihood based on segments and grid specifications
def generate_measurement_likelihood(segments, road_spec, grid_spec):
    measurement_likelihood = np.zeros(grid_spec["d"].shape)

    for segment in segments:
        d_i, phi_i = generate_vote(segment, road_spec)

        if (
            d_i > grid_spec["d_max"]
            or d_i < grid_spec["d_min"]
            or phi_i < grid_spec["phi_min"]
            or phi_i > grid_spec["phi_max"]
        ):
            continue

        i = int((d_i - grid_spec["d_min"]) / grid_spec["delta_d"])
        j = int((phi_i - grid_spec["phi_min"]) / grid_spec["delta_phi"])

        if 0 <= i < grid_spec["d"].shape[0] and 0 <= j < grid_spec["d"].shape[1]:
            measurement_likelihood[i, j] += 1

    if np.linalg.norm(measurement_likelihood) == 0:
        return None

    measurement_likelihood /= np.sum(measurement_likelihood)
    return measurement_likelihood


# Function to update the belief based on the current segments, road specifications, and grid specifications
def histogram_update(belief, segments, road_spec, grid_spec):
    segmentsArray = prepare_segments(segments, grid_spec)
    measurement_likelihood = generate_measurement_likelihood(segmentsArray, road_spec, grid_spec)

    if measurement_likelihood is not None:
        belief = measurement_likelihood * belief
        belief /= np.sum(belief)
    return measurement_likelihood, belief


# Function to calculate the distance between segment points
def getSegmentDistance(segment):
    x_c = (segment.points[0].x + segment.points[1].x) / 2
    y_c = (segment.points[0].y + segment.points[1].y) / 2
    return sqrt(x_c**2 + y_c**2)

