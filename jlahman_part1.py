# Joshua Lahman
# CS2300 Programming Assignment #3
# Part 1


# Cramer's Rule 2x2
def cramer2(n11, n12, n13, n21, n22, n23):
    # Find determinants of 3 matrices
    deta = n11 * n22 - n21 * n12
    deta1 = n13 * n22 - n23 * n12
    deta2 = n11 * n23 - n21 * n13

    # calculate eigenvalues
    x1 = deta1 / deta
    x2 = deta2 / deta

    return [x1, x2]


# set file name to variable----------------------------------------------------
txt = 'pa3_test_input_1.txt'

# open txt file and copy data
with open(txt, 'r') as f:
    data = f.readlines()  # read raw lines into an array

# organize data into n-dimension array
matrix = []
intCount = 0
for raw_line in data:
    split_line = raw_line.strip().split(" ")  # ["1", "0" ... ]
    # loop to count number of items in matrix
    for x in split_line:
        intCount = intCount + 1
    # format matrix
    nums_ls = [int(x.replace('"', '')) for x in split_line]
    matrix.append(nums_ls)

# 2x3 system of equations solver
determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
determinant1 = matrix[0][2] * matrix[1][1] - matrix[1][2] * matrix[0][1]
determinant2 = matrix[0][0] * matrix[1][2] - matrix[1][0] * matrix[0][2]

# check if system can be solved
if determinant == 0:
    if determinant1 == 0 & determinant2 == 0:
        print("system inconsistent")
    else:
        print("system undetermined")
else:
    # Test 2x2
    [ans1, ans2] = cramer2(matrix[0][0], matrix[0][1], matrix[0][2], matrix[1][0], matrix[1][1], matrix[1][2])
    print(str(ans1) + " " + str(ans2))
