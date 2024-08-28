from typing import Tuple
import numpy as np

def PIDController(
        v_0: float,
        theta_ref: float,
        theta_hat: float,
        prev_e: float,
        prev_int: float,
        delta_t: float,
        Kp: float = 1.0,
        Ki: float = 0.1,
        Kd: float = 0.01
) -> Tuple[float, float, float, float]:
    """
    PID performing heading control.
    Args:
        v_0:        linear Duckiebot speed (given).
        theta_ref:  reference heading pose.
        theta_hat:  the current estimated theta.
        prev_e:     tracking error at previous iteration.
        prev_int:   previous integral error term.
        delta_t:    time interval since last call.
        Kp:         proportional gain.
        Ki:         integral gain.
        Kd:         derivative gain.
    Returns:
        v_0:     linear velocity of the Duckiebot
        omega:   angular velocity of the Duckiebot
        e:       current tracking error (automatically becomes prev_e at next iteration).
        e_int:   current integral error (automatically becomes prev_int at next iteration).
    """

    # Calculate the current error
    e = theta_ref - theta_hat

    # Calculate the integral of the error
    e_int = prev_int + e * delta_t

    # Calculate the derivative of the error
    e_deriv = (e - prev_e) / delta_t

    # Calculate the control output (omega)
    omega = Kp * e + Ki * e_int + Kd * e_deriv

    # Print for debugging
    # print(f"\n\nDelta time : {delta_t} \nE : {np.rad2deg(e)} \nE int : {e_int} \nPrev e : {prev_e} \nOmega : {omega} \nTheta hat: {np.rad2deg(theta_hat)} \n")

    return v_0, omega, e, e_int

