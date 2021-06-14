#!/usr/bin/env python
import numpy as np
from sympy.matrices import Matrix
from sympy import symbols, atan2, sqrt


# Fixed Axis X-Y-Z Rotation Matrix
R_XYZ = Matrix([[ 0.353553390593274, -0.306186217847897, 0.883883476483184],
            [ 0.353553390593274,  0.918558653543692, 0.176776695296637],
            [-0.866025403784439,               0.25, 0.433012701892219]])

######## TO DO ##########
# Calculate the Euler angles that produces a rotation equivalent to R (above)
# NOTE: Be sure your answer has units of DEGREES!
alpha = 180/np.pi*(atan2(R_XYZ[1,0], R_XYZ[0,0])) # rotation about Z-axis
beta  = 180/np.pi*(atan2(-R_XYZ[2,0], sqrt(R_XYZ[0,0]*R_XYZ[0,0]+R_XYZ[1,0]*R_XYZ[1,0]))) # rotation about Y-axis
gamma = 180/np.pi*(atan2(R_XYZ[2,1], R_XYZ[2,2])) # rotation about X-axis

print(alpha)
print(beta)
print(gamma)


