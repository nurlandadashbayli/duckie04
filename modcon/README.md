# Duckietown Modeling and Control Challenge

This project involves modeling and controlling a Duckiebot to navigate its environment effectively. The process includes calibrating the wheels, tracking the robot's position using odometry, and fine-tuning a PID controller for precise movement control. This `README.md` file provides a comprehensive guide to the steps taken to achieve these tasks.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Steps](#steps)
  - [1. Wheel Calibration](#1-wheel-calibration)
  - [2. Odometry](#2-odometry)
  - [3. PID Controller](#3-pid-controller)
- [Running the Code](#running-the-code)
- [Testing on a Physical Robot](#testing-on-a-physical-robot)
- [Conclusion](#conclusion)

## Overview

In this challenge, the Duckiebot is programmed to navigate its environment using a combination of wheel calibration, odometry, and a PID controller. The key steps in this process are:

1. **Wheel Calibration** - Ensures the Duckiebot drives straight and minimizes slippage.
2. **Odometry** - Tracks the Duckiebot’s position and orientation in real-time.
3. **PID Controller** - Adjusts the Duckiebot's speed and direction to follow a desired path and avoid collisions.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- Duckietown ROS Packages
- Basic understanding of robotics and control systems

## Setup

1. **Clone the repository** (if this is part of a repository):
   ```bash
   git clone https://github.com/dadashbaylinurlan/duckie04.git
   cd modcon
   ```

2. **Ensure your Duckiebot is properly configured** with ROS and all necessary Duckietown packages.

## Steps

### 1. Wheel Calibration

Wheel calibration is the first step to ensure that the Duckiebot drives straight and reduces any bias or slippage. Calibration involves adjusting the motor parameters so that both wheels move synchronously.

- **Procedure**:
  - Use the `wheels_calibration.ipynb` notebook to run the calibration routine.
  - Observe the Duckiebot’s initial biased movement (e.g., pulling to the right).
  - Adjust wheel speed parameters according to the calibration instructions from Duckietown.
  - Re-run the calibration to check improvements.

- **Code Snippet**:
  ```python
  # Example from wheels_calibration.ipynb
  def calibrate_wheels():
      # Adjust wheel speeds
      left_wheel_speed = adjust_speed(left_initial_speed)
      right_wheel_speed = adjust_speed(right_initial_speed)
      apply_calibration(left_wheel_speed, right_wheel_speed)
  ```

### 2. Odometry

Odometry is used to track the Duckiebot’s position and orientation in real-time, providing feedback for navigation and control.

- **Procedure**:
  - Manually drive the Duckiebot using the keyboard while tracking its position.
  - Use the `odometry_activity.ipynb` notebook to visualize the Duckiebot’s movement and update its position in real-time.
  - Ensure that the odometry data accurately reflects the Duckiebot’s movements.

- **Code Snippet**:
  ```python
  # Example from odometry_activity.ipynb
  def update_odometry():
      current_position = get_current_position()
      update_position(current_position)
      display_position_on_map(current_position)
  ```

### 3. PID Controller

The PID controller is designed to adjust the Duckiebot's speed and direction dynamically, helping it follow a designated path and avoid obstacles.

- **Procedure**:
  - Implement the PID control logic in `pid_controller.py` to adjust the robot's velocity and heading.
  - Test the Duckiebot’s response to various PID parameter settings.
  - Fine-tune the PID parameters to balance movement accuracy and effective tracking.
  - Resolve any issues such as spinning in place or inaccurate tracking by adjusting PID values.

- **Code Snippet**:
  ```python
  # Example from pid_controller.py
  def pid_control(target_velocity, target_heading):
      error = compute_error(current_state, target_state)
      control_signal = compute_pid(error)
      apply_control_signal(control_signal)
  ```

## Running the Code

To run the code, follow the instructions in the Jupyter Notebooks for calibration and odometry, and then test the PID controller using the provided Python scripts.

## Testing on a Physical Robot

You can test your agent on the robot using the following commands:

1. **Run everything on the robot**:
   ```bash
   dts code workbench --duckiebot YOUR_DUCKIEBOT
   ```

   This command runs both the drivers and the agent directly on the Duckiebot.

2. **Run the agent locally, drivers on the robot**:
   ```bash
   dts code workbench --duckiebot YOUR_DUCKIEBOT --local
   ```

   This command runs the Duckiebot’s drivers on the robot while executing the agent code on your local machine (laptop).

Ensure to replace `YOUR_DUCKIEBOT` with the name of your Duckiebot.

## Conclusion

By following these steps, the Duckiebot can effectively navigate its environment using calibrated wheel settings, accurate odometry for position tracking, and a fine-tuned PID controller for dynamic movement control. Adjusting the PID parameters is crucial for balancing the trade-offs between movement accuracy and tracking reliability.


---

**Author**: Nurlan Dadashbayli
