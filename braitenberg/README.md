# Braitenberg Challenge

This project demonstrates the use of HSV (Hue, Saturation, Value) color space settings for image processing to help a Duckiebot detect and avoid obstacles in its path, specifically focusing on identifying ducks in the environment. This `README.md` provides a step-by-step guide to setting up and refining the robot's behavior to navigate around detected obstacles effectively.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Steps](#steps)
  - [1. Adjusting HSV Settings](#1-adjusting-hsv-settings)
  - [2. Fine-Tuning Preprocessing](#2-fine-tuning-preprocessing)
  - [3. Configuring Robot's Behavior](#3-configuring-robots-behavior)
- [Running the Code](#running-the-code)
- [Testing on a Physical Robot](#testing-on-a-physical-robot)
- [Conclusion](#conclusion)

## Overview

In this challenge, the Duckiebot is programmed to detect and avoid obstacles using HSV color space adjustments for image processing. The key steps in this process include adjusting HSV settings, fine-tuning image preprocessing, and configuring the robot's behavior through motor control settings.

1. **Adjusting HSV Settings** - Filters the image to isolate the target object (a duck) by adjusting HSV color values.
2. **Fine-Tuning Preprocessing** - Applies the HSV settings to the robot's vision system for optimal detection.
3. **Configuring Robot's Behavior** - Determines how the robot should respond when an obstacle (duck) is detected.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- OpenCV
- Duckietown ROS Packages
- Basic understanding of image processing and robot control systems

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dadashbaylinurlan/duckie04.git
   cd braitenberg
   ```

2. **Ensure your Duckiebot is properly configured** with ROS and all necessary Duckietown packages.

## Steps

### 1. Adjusting HSV Settings

The first step involves adjusting HSV settings for image processing to help the robot detect obstacles effectively. HSV color space is beneficial as it separates color information from intensity, making it easier to detect objects under varying lighting conditions.

- **Procedure**:
  - Start with an image of a duck and adjust the HSV values using the `braitenberg02.ipynb` notebook.
  - Fine-tune the HSV parameters to filter out the background and isolate the duck.

- **Code Snippet**:
  ```python
  # Example from braitenberg02.ipynb
  def adjust_hsv(image):
      hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(hsv, lower_bound, upper_bound)
      result = cv2.bitwise_and(image, image, mask=mask)
      return result
  ```

### 2. Fine-Tuning Preprocessing

Once the optimal HSV values are determined, adjust these parameters in the preprocessing file to apply them to the robot's vision system.

- **Procedure**:
  - Use the `preprocessing.py` script to set the optimal HSV values for detecting ducks.
  - Fine-tune the preprocessing steps to ensure the robot can effectively filter out unnecessary elements and focus on detecting ducks.

- **Code Snippet**:
  ```python
  # Example from preprocessing.py
  def preprocess_image(image):
      hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
      mask = cv2.inRange(hsv, optimal_lower_bound, optimal_upper_bound)
      processed_image = cv2.bitwise_and(image, image, mask=mask)
      return processed_image
  ```

### 3. Configuring Robot's Behavior

After preprocessing is fine-tuned, the next step is to configure how the robot's motors respond to the processed images, dictating how the robot reacts when a duck is detected.

- **Procedure**:
  - Adjust motor response settings in the `connections.py` file.
  - Experiment with different configurations to ensure smooth navigation around detected obstacles.

- **Code Snippet**:
  ```python
  # Example from connections.py
  def control_motors(sensor_input):
      if sensor_input == "duck_detected":
          left_motor_speed = calculate_speed_left()
          right_motor_speed = calculate_speed_right()
          apply_motor_control(left_motor_speed, right_motor_speed)
  ```

## Running the Code

To run the code, follow the instructions in the Jupyter Notebooks to adjust HSV settings and preprocess images. Then, configure the robot's behavior using the provided Python scripts.

## Testing on a Physical Robot

You can test the Braitenberg challenge on a Duckiebot using the following commands:

1. **Run everything on the robot**:
   ```bash
   dts code workbench --duckiebot YOUR_DUCKIEBOT
   ```

   This command runs both the drivers and the agent directly on the Duckiebot.

2. **Run the agent locally, drivers on the robot**:
   ```bash
   dts code workbench --duckiebot YOUR_DUCKIEBOT --local
   ```

   This command runs the Duckiebot’s drivers on the robot while executing the code on your local machine (laptop).

Ensure to replace `YOUR_DUCKIEBOT` with the name of your Duckiebot.

## Conclusion

By following these steps, the Duckiebot can detect and avoid obstacles using HSV color space adjustments and image processing techniques. Although initial trials showed effective detection of ducks, further refinements are needed to ensure smooth and continuous navigation around obstacles.


---

**Author**: Nurlan Dadashbayli
