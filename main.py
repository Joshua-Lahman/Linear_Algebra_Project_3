# Joshua Lahman
# CS2300 Programming Assignment #3
# Part 3

import math


# Find Determinant 2x2
def det(n11, n12, n21, n22):
    return n11 * n22 - n21 * n12


# Find Determinant 3x3
def det3(n11, n12, n13, n21, n22, n23, n31, n32, n33):
    # Find the 2x2 determinants and multiply by scalar
    deta = n11 * det(n22, n23, n32, n33)
    detb = n12 * det(n21, n23, n31, n33)
    detc = n13 * det(n21, n22, n31, n32)
    ans = deta - detb + detc

    return ans


# set file name to variable
txt = 'pa3_test_input_1.txt'  # Will not work with text files that contain whitespace
# 3D_test_input_1.txt
# pa3_test_input_1.txt

# open txt file and copy data
with open(txt, 'r') as f:
    data = f.readlines()

# organize data into 2d array
matrix = []
for raw_line in data:
    split_line = raw_line.strip().split(" ")
    nums_ls = [int(x.replace('"', '')) for x in split_line]
    matrix.append(nums_ls)

# determine matrix size
count = 0
for x in matrix:
    for j in x:
        count += 1

# 2x3 matrix triangle area
if count == 6:
    # find determinant of 3x3 filling missing values with 1
    triDet = det3(1, 1, 1, matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2])

    # find area
    area = 1/2 * triDet

# 3x3 matrix triangle area
elif count == 9:
    # find length of two sides
    sideA = [matrix[1][0] - matrix[0][0], matrix[1][1] - matrix[0][1], matrix[1][2] - matrix[0][2]]
    sideB = [matrix[2][0] - matrix[0][0], matrix[2][1] - matrix[0][1], matrix[2][2] - matrix[0][2]]

    # take 3 determinants
    deter1 = det(sideA[1], sideA[2], sideB[1], sideB[2])
    deter2 = det(sideA[0], sideA[2], sideB[0], sideB[2])
    deter3 = det(sideA[0], sideA[1], sideB[0], sideB[1])

    # calculate area of triangle
    area = math.sqrt((deter1*deter1) + (deter2*deter2) + (deter3*deter3)) / 2
else:
    print("matrix size error")
print(area)

# 2x3 matrix line
if count == 6:
    slope = matrix[1][0] - matrix[0][0] / matrix[1][1] - matrix[0][1]
    yIntercept = -1 * matrix[0][1] * slope + matrix[0][0]
    print("y = " + str(slope) + "x + " + str(yIntercept))

# 3x3 matrix plane
elif count == 9:
    slope = -1 / (matrix)