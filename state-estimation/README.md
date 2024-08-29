# State Estimating from Duckietown Challenge

This project demonstrates the use of a histogram filter to detect lines on the ground and estimate the Duckiebot’s position. A histogram filter is a probabilistic technique that helps determine where the robot is most likely located by analyzing its camera view. This `README.md` file provides a step-by-step guide to implementing and understanding the histogram filter technique used in this project.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Steps](#steps)
  - [1. Initialize Belief Distribution](#1-initialize-belief-distribution)
  - [2. Prediction Step](#2-prediction-step)
  - [3. Update Step](#3-update-step)
- [Running the Code](#running-the-code)
- [Testing on a Physical Robot](#testing-on-a-physical-robot)
- [Conclusion](#conclusion)

## Overview

In this challenge, the Duckiebot uses a histogram filter to estimate its position on the ground by detecting lines and adjusting its belief about its location. The key steps in this process are:

1. **Initialize Belief Distribution** - Represents the initial guess about the Duckiebot’s location.
2. **Prediction Step** - Uses the robot's motion model to predict potential movements and adjust the belief state.
3. **Update Step** - Refines the belief using sensor data, such as the detection of lines on the ground.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- Duckietown ROS Packages
- Basic understanding of probability and state estimation techniques

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dadashbaylinurlan/duckie04.git
   cd state-estimation
   ```

2. **Ensure your Duckiebot is properly configured** with ROS and all necessary Duckietown packages.

## Steps

### 1. Initialize Belief Distribution

The belief distribution represents an initial guess about the Duckiebot’s location. It is a probability distribution over the possible locations where the Duckiebot could be.

- **Procedure**:
  - Initialize a uniform belief distribution using the `histogram_filter.ipynb` notebook.
  - This initial distribution assumes that the Duckiebot could be anywhere with equal probability.

- **Code Snippet**:
  ```python
  # Example from histogram_filter.ipynb
  def initialize_belief():
      belief = np.ones(grid_size) / grid_size
      return belief
  ```

### 2. Prediction Step

The prediction step uses the robot’s motion model to predict where the Duckiebot might be based on its previous movements and control inputs.

- **Procedure**:
  - Implement the prediction logic in the `histogram_filter.py` script.
  - Update the belief distribution based on the Duckiebot’s motion and control inputs.

- **Code Snippet**:
  ```python
  # Example from histogram_filter.py
  def prediction_step(belief, control_input):
      predicted_belief = apply_motion_model(belief, control_input)
      return predicted_belief
  ```

### 3. Update Step

The update step refines the belief distribution using new sensor data from the Duckiebot’s camera, which detects lines on the ground.

- **Procedure**:
  - Implement the update logic in the `histogram_filter.py` script.
  - Use sensor readings to adjust the belief distribution, enhancing the estimate of the Duckiebot's position.

- **Code Snippet**:
  ```python
  # Example from histogram_filter.py
  def update_step(belief, sensor_data):
      updated_belief = apply_sensor_model(belief, sensor_data)
      return updated_belief
  ```

## Running the Code

To run the code, follow the instructions in the Jupyter Notebook for initializing the belief distribution and implementing the prediction and update steps using the provided Python script.

## Testing on a Physical Robot

You can test the histogram filter on a Duckiebot using the following commands:

1. **Run everything on the robot**:
   ```bash
   dts code workbench --duckiebot YOUR_DUCKIEBOT
   ```

   This command runs both the drivers and the agent directly on the Duckiebot.

2. **Run the agent locally, drivers on the robot**:
   ```bash
   dts code workbench --duckiebot YOUR_DUCKIEBOT --local
   ```

   This command runs the Duckiebot’s drivers on the robot while executing the histogram filter code on your local machine (laptop).

Ensure to replace `YOUR_DUCKIEBOT` with the name of your Duckiebot.

## Conclusion

By following these steps, the Duckiebot can estimate its position on the ground more accurately using a histogram filter that combines prediction and update steps. This approach is crucial for autonomous robots as it helps them understand and adapt to their surroundings, whether in a controlled simulation or a real-world environment.


---

**Author**: Nurlan Dadashbayli
