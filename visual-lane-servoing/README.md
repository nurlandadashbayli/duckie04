# Duckietown Visual Lane Servoing Task

This project demonstrates a visual lane servoing task for a Duckiebot in the Duckietown environment. The Duckiebot uses its camera to navigate accurately within a designated path by employing a series of calibrations and image processing techniques. This `README.md` will guide you through the steps taken to achieve successful lane following using visual servoing.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Steps](#steps)
  - [1. Intrinsic Camera Calibration](#1-intrinsic-camera-calibration)
  - [2. Extrinsic Camera Calibration](#2-extrinsic-camera-calibration)
  - [3. Image Filtering](#3-image-filtering)
  - [4. Visual Servoing](#4-visual-servoing)
- [Running the Code](#running-the-code)
- [Testing on a Physical Robot](#testing-on-a-physical-robot)
- [Conclusion](#conclusion)

## Overview

In this project, the Duckiebot is programmed to move accurately within a designated path using visual feedback. The process involves several key steps:

1. **Intrinsic Camera Calibration** - Corrects lens distortions to ensure accurate environmental perception.
2. **Extrinsic Camera Calibration** - Aligns the camera's view with the robot's perspective for accurate navigation.
3. **Image Filtering** - Processes images to highlight important details and remove noise.
4. **Visual Servoing** - Allows the Duckiebot to adjust its movements in real-time based on visual input.

## Prerequisites

- Python 3.x
- Jupyter Notebook
- OpenCV
- Duckietown ROS Packages
- Camera Calibration patterns (Checkerboard or other suitable patterns)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/dadashbaylinurlan/duckie04.git
   cd visual-lane-servoing
   ```

2. **Ensure your Duckiebot is properly configured** with ROS and all necessary Duckietown packages.

## Steps

### 1. Intrinsic Camera Calibration

Intrinsic calibration corrects lens distortions, ensuring the Duckiebot can accurately interpret its environment. This step involves moving the robot around a calibration pattern and recording images to adjust for any camera distortions.

- **Procedure**:
  - Move the Duckiebot in front of a calibration pattern (checkerboard).
  - Capture images from various angles and distances.
  - Use the `camera_calibration.ipynb` notebook to process these images and compute the intrinsic parameters.
  - Save the calibration file for future use.

- **Code Snippet**:
  ```python
  # Example from camera_calibration.ipynb
  # Perform intrinsic calibration
  intrinsic_parameters = calibrate_camera(images)
  save_calibration(intrinsic_parameters, 'intrinsic_calibration.yaml')
  ```

### 2. Extrinsic Camera Calibration

Extrinsic calibration aligns the camera's position and orientation with the Duckiebot's body, ensuring accurate perception of the environment from the robot's perspective.

- **Procedure**:
  - Position the Duckiebot on designated arrows in the Duckietown setup.
  - Use the `camera_calibration.ipynb` notebook to calibrate the camera relative to the robot's position.
  - Save the extrinsic calibration data.

- **Code Snippet**:
  ```python
  # Example from camera_calibration.ipynb
  # Perform extrinsic calibration
  extrinsic_parameters = calibrate_extrinsic(robot_position, camera_position)
  save_calibration(extrinsic_parameters, 'extrinsic_calibration.yaml')
  ```

### 3. Image Filtering

Image filtering is essential for removing noise and highlighting the lane markings that the Duckiebot needs to follow. This process involves using filters to isolate the yellow and white lane lines.

- **Procedure**:
  - Capture a test image from the Duckiebot's camera.
  - Apply filtering techniques such as Gaussian blur, color thresholding, and edge detection.
  - Use the `image_filtering.ipynb` notebook to adjust parameters and visualize results.

- **Code Snippet**:
  ```python
  # Example from image_filtering.ipynb
  filtered_image = apply_filters(test_image)
  display_image(filtered_image)
  ```

### 4. Visual Servoing

In the visual servoing phase, the Duckiebot uses real-time visual feedback to adjust its path. The calibrated camera and filtered images guide the Duckiebot to stay within the lane markings.

- **Procedure**:
  - Combine intrinsic and extrinsic calibration results with the filtered images.
  - Implement control logic in the Python script (`visual_servoing_activity.py`) to adjust the Duckiebot’s steering and speed.
  - Run the visual servoing script to observe the Duckiebot navigating the path.

- **Code Snippet**:
  ```python
  # Example from visual_servoing_activity.py
  def main():
      initialize_robot()
      while True:
          image = capture_image()
          processed_image = process_image(image)
          control_commands = compute_control(processed_image)
          apply_control(control_commands)
  ```

## Running the Code

To run the code, follow the steps in the Jupyter Notebooks and then use the commands provided in the next section to test your Duckiebot.

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

By following these steps, the Duckiebot can navigate a designated path using visual servoing techniques, combining camera calibration and image processing to interpret and respond to its environment in real-time. 

---

**Author**: Nurlan Dadashbayli
