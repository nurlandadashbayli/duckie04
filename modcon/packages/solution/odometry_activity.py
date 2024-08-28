from typing import Tuple
import numpy as np

def delta_phi(ticks: int, prev_ticks: int, resolution: int) -> Tuple[float, int]:
    """
    Args:
        ticks: Current tick count from the encoders.
        prev_ticks: Previous tick count from the encoders.
        resolution: Number of ticks per full wheel rotation returned by the encoder.
    Return:
        dphi: Rotation of the wheel in radians.
        ticks: Current number of ticks.
    """
    # Calculate the difference in ticks
    delta_ticks = ticks - prev_ticks
    
    # Compute the rotation in radians
    dphi = (2 * np.pi * delta_ticks) / resolution
    
    return dphi, ticks

def pose_estimation(
    R: float,
    baseline: float,
    x_prev: float,
    y_prev: float,
    theta_prev: float,
    delta_phi_left: float,
    delta_phi_right: float,
) -> Tuple[float, float, float]:
    """
    Calculate the current Duckiebot pose using the dead-reckoning model.

    Args:
        R:                  Radius of wheel (both wheels are assumed to have the same size).
        baseline:           Distance from wheel to wheel; 2L of the theory.
        x_prev:             Previous x estimate.
        y_prev:             Previous y estimate.
        theta_prev:         Previous orientation estimate.
        delta_phi_left:     Left wheel rotation (rad).
        delta_phi_right:    Right wheel rotation (rad).

    Return:
        x_curr:             Estimated x coordinate.
        y_curr:             Estimated y coordinate.
        theta_curr:         Estimated heading.
    """
    # Calculate distances each wheel has traveled
    dL = R * delta_phi_left
    dR = R * delta_phi_right
    
    # Calculate change in orientation
    delta_theta = (dR - dL) / baseline
    
    # Calculate average distance traveled
    d = (dR + dL) / 2
    
    # Update position
    x_curr = x_prev + d * np.cos(theta_prev + delta_theta / 2)
    y_curr = y_prev + d * np.sin(theta_prev + delta_theta / 2)
    
    # Update orientation
    theta_curr = theta_prev + delta_theta
    
    return x_curr, y_curr, theta_curr

