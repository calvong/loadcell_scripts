# calibrate loadcell

import numpy as np

def get_coeff(t1, m1, t2, m2):
    # t for true value
    # m for measured value
    a = np.array([[m1, 1], [m2, 1]])
    b = np.array([t1, t2])
    x = np.linalg.solve(a, b)

    return x

def read_calibration():
    coeff = []
    cfile = open("calibration.txt", 'r')
    line = cfile.readline()

    l = line.split(',')

    for b in range(8):
        coeff.append(float(l[b]))

    cfile.close()

    return coeff

def run_calibration(mvalue):
    coeff = []

    print "running calibration ..."

    for i in range(4):  # for 4 loadcells
        val_t1 = 664
        val_m1 = mvalue[2*i]

        val_t2 = 893
        val_m2 = mvalue[2*i+1]

        c = get_coeff(val_t1, val_m1, val_t2, val_m2)

        coeff.append(c[0])
        coeff.append(c[1])

    cfile = open("calibration.txt", 'w')

    for a in range(7):
        cfile.write(str(coeff[a]) + ',')

    cfile.write(str(coeff[7]))
    cfile.close()


    return coeff
