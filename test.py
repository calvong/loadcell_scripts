import numpy as np
import calibration_helper as cali

x = cali.get_coeff(9,3,8,1)

print(x)


d = cali.run_calibration()
print d