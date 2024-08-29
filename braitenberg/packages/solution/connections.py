from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # Creating the weight matrix for the left motor
    res = np.zeros(shape=shape, dtype="float32")
    # Example logic: apply specific weights to the matrix
    res[:shape[0]//2, :] = 1  # Top half of the image
    res[shape[0]//2:, :] = 0.5  # Bottom half of the image
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # Creating the weight matrix for the right motor
    res = np.zeros(shape=shape, dtype="float32")
    # Example logic: apply specific weights to the matrix
    res[:shape[0]//2, :] = 0.5  # Top half of the image
    res[shape[0]//2:, :] = 1  # Bottom half of the image
    return res

