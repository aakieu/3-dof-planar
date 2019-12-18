from numpy import *   # imports all function so we don't have to use np.function()

# Link lengths
a1 = 6.2  # length of link a1 in cm
a2 = 5.2  # length of link a2 in cm
a3 = 0  # length of link a3 in cm
a4 = 6.9  # length of link a4 in cm
a5 = 0  # length of link a5 in cm
a6 = 6.8  # length of link a6 in cm

# Angles
theta_1 = 90  # theta 1 angle in degrees
theta_2 = 90  # theta 2 angle in degrees
theta_3 = 90  # theta 3 angle in degrees

theta_1 = (theta_1/180)*pi  # theta 1 in radians
theta_2 = (theta_2/180)*pi  # theta 2 in radians
theta_3 = (theta_3/180)*pi  # theta 3 in radians

# DH Parameter Table for 3 DOF Planar
PT = [[theta_1, 0, a2, a1],
      [theta_2, 0, a4, a3],
      [theta_3, 0, a6, a5]]

# Homogeneous Transformation Matrices
i = 0
H0_1 = [[cos(PT[i][0]), -sin(PT[i][0])*cos(PT[i][1]), sin(PT[i][0])*sin(PT[i][1]), PT[i][2]*cos(PT[i][0])],
        [sin(PT[i][0]), cos(PT[i][0])*cos(PT[i][1]), -cos(PT[i][0])*sin(PT[i][1]), PT[i][2]*sin(PT[i][0])],
        [0, sin(PT[i][1]), cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]

i = 1
H1_2 = [[cos(PT[i][0]), -sin(PT[i][0])*cos(PT[i][1]), sin(PT[i][0])*sin(PT[i][1]), PT[i][2]*cos(PT[i][0])],
        [sin(PT[i][0]), cos(PT[i][0])*cos(PT[i][1]), -cos(PT[i][0])*sin(PT[i][1]), PT[i][2]*sin(PT[i][0])],
        [0, sin(PT[i][1]), cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]

i = 2
H2_3 = [[cos(PT[i][0]), -sin(PT[i][0])*cos(PT[i][1]), sin(PT[i][0])*sin(PT[i][1]), PT[i][2]*cos(PT[i][0])],
        [sin(PT[i][0]), cos(PT[i][0])*cos(PT[i][1]), -cos(PT[i][0])*sin(PT[i][1]), PT[i][2]*sin(PT[i][0])],
        [0, sin(PT[i][1]), cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]]

print("H0_1 =")
print(matrix(H0_1))
print("H1_2 =")
print(matrix(H1_2))
print("H2_3 =")
print(matrix(H2_3))

H0_2 = dot(H0_1,H1_2)
H0_3 = dot(H0_2,H2_3)

print("H0_3 =")
print(matrix(H0_3))
