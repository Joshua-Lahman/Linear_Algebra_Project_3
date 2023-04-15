# Joshua Lahman
# CS2300 Programming Assignment #3
# Part 2

import math


# find polynomial for eigen values
def polynomial(n11, n12, n21, n22):
    a = 1
    b = -1 * (n11 + n22)
    c = (-1 * (n12*n21)) + (n11*n22)
    return [a, b, c]


# quadratic equation
def quad(a, b, c):
    var1 = ((-1)*b + math.sqrt(b*b - 4*a*c)) / (2*a)
    var2 = ((-1)*b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return [var1, var2]


# set file name to variable
txt = 'pa3_test_input_1.txt'  # Will not work with text files that contain whitespace

# open txt file and copy data
with open(txt, 'r') as f:
    data = f.readlines()

# organize data into 2d array
matrix = []
for raw_line in data:
    split_line = raw_line.strip().split(" ")
    nums_ls = [int(x.replace('"', '')) for x in split_line]
    matrix.append(nums_ls)

# find eigen values-----------------------------------------------------
# create polynomial to find lambda values
poly = polynomial(matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1])

# calculate lambda using quadratic formula
lamb = quad(poly[0], poly[1], poly[2])

# set dominant eigenvector to index 0
eigenvalues = [lamb[0], lamb[1]]
if abs(lamb[0]) < abs(lamb[1]):
    eigenvalues[0] = lamb[1]
    eigenvalues[1] = lamb[0]

# create matrix for eigenvalues
eigenMatrix = []
eigenMatrix = [lamb[0], matrix[0][1]], [matrix[1][0], lamb[1]]

# find eigenvectors
realEigen = True
flipV = False
eigenVectors = []
for i in range(0, 2):
    # construct matrix to find eigenvectors
    lambMatrix = []
    lambMatrix = [[matrix[0][0] - lamb[i], matrix[0][1]], [matrix[1][0], matrix[1][1] - lamb[i]]]

    # make sure a1,1 != 0
    vectorMatrix = []
    if lambMatrix[0][0] == 0:
        if lambMatrix[1][0] == 0:
            realEigen = False
        # row exchange if a1,1 == 0
        vectorMatrix = [[lambMatrix[1][0], lambMatrix[1][1]], [lambMatrix[0][0], lambMatrix[0][1]]]
        flipV = True

    else:
        # no row exchange needed
        vectorMatrix = [[lambMatrix[0][0], lambMatrix[0][1]], [lambMatrix[1][0], lambMatrix[1][1]]]
        flipV = False

    # Sheer r2 = (-a2,1/a1,1 * r1) + r2
    sheer = (-1)*vectorMatrix[1][0] / vectorMatrix[0][0]
    vectorMatrix[1][0] = (sheer * vectorMatrix[0][0]) + vectorMatrix[1][0]
    vectorMatrix[1][1] = (sheer * vectorMatrix[0][1]) + vectorMatrix[1][1]

    # let v2 = 1 for back substitution
    v1 = 0
    v2 = 0
    if vectorMatrix[1][1] == 0:
        v2 = 1
    else:
        v2 = 0

    # back substitution
    v1 = ((-1) * (eigenMatrix[0][1]) * v2) / eigenMatrix[0][0]
    v = [v1, v2]

    # append eigenvectors to matrix
    eigenVectors.append(v)

# flip eigen vector matrix if used a row exchange
if flipV:
    temp = eigenVectors[0]
    eigenVectors[0] = eigenVectors[1]
    eigenVectors[1] = temp

# find transpose of eigenvector matrix
transposeEVMatrix = [[eigenVectors[0][0], eigenVectors[1][0]], [eigenVectors[0][1], eigenVectors[1][1]]]

# if there is a real eigenvalue, print results
if realEigen:
    print(str("%.4f  %.4f" % (eigenMatrix[0][0], eigenMatrix[0][1])))
    print(str("%.4f  %.4f" % (eigenMatrix[1][0], eigenMatrix[1][1])))
    print(str("%.4f  %.4f" % (eigenVectors[0][0], eigenVectors[0][1])))
    print(str("%.4f  %.4f" % (eigenVectors[1][0], eigenVectors[1][1])))
    print(str("%.4f  %.4f" % (transposeEVMatrix[0][0], transposeEVMatrix[0][1])))
    print(str("%.4f  %.4f" % (transposeEVMatrix[1][0], transposeEVMatrix[1][1])))
else:
    print('No real eigenvalues')
