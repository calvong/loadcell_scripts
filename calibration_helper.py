# calibrate loadcell

import numpy as np

def get_coeff(t1, m1, t2, m2):
    # t for true value
    # m for measured value
    a = np.array([[m1, 1], [m2, 1]])
    b = np.array([t1, t2])
    x = np.linalg.solve(a, b)

    return x

def run_calibration():
    coeff = []

    for i in range(4):  # for 4 loadcells
        coeff.append(i)

    return coeff