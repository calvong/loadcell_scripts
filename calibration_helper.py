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

    runCali = raw_input("Run calibration? y/n : ")

    if runCali == 'y':
        for i in range(4):  # for 4 loadcells
            print "For loadcell %d" % (i+1)
            val_t1 = float(input("Input true value1: "))
            val_m1 = float(input("Input measured value1: "))

            val_t2 = float(input("Input true value2: "))
            val_m2 = float(input("Input measured value2: "))

            c = get_coeff(val_t1, val_m1, val_t2, val_m2)

            coeff.append(c[0])
            coeff.append(c[1])

        cfile = open("calibration.txt", 'w')

        for a in range(7):
            cfile.write(str(coeff[a]) + ',')

        cfile.write(str(coeff[7]))
        cfile.close()

    elif runCali == 'n':
        print "Not running calibration"

        cfile = open("calibration.txt", 'r')
        line = cfile.readline()

        l = line.split(',')

        for b in range(8):
            coeff.append(float(l[b]))

        cfile.close()

    return coeff
