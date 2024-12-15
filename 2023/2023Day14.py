with open("input.in", "r") as file:
    lines = file.read().split("\n")
    lines = [list(line) for line in lines]
import functools
from copy import deepcopy


def rotate(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # Transpose the matrix
    transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
    # Reverse each row
    rotated_matrix = [[row[i]
                       for i in range(m - 1, -1, -1)] for row in transposed_matrix]
    return rotated_matrix


def display(matrix):
    for r in range(len(matrix)):
        row = ""
        for c in range(len(matrix[0])):
            row += matrix[r][c]
        print(row)
    print("\n")


def cycle(lines):
    for i in range(4):
        for r, line in enumerate(lines):
            # for each rock, move it forwards until it hits a #, O or the end of the file
            for c, rock in enumerate(line):
                if rock == "O":
                    ry, rx = r, c
                    while True:
                        # if the square N of the rock is a hash or EoF
                        if ry-1 < 0:
                            break
                        elif lines[ry-1][rx] == "#":
                            break
                        elif lines[ry-1][rx] == "O":
                            break
                        else:
                            lines[ry-1][rx] = "O"
                            lines[ry][rx] = "."
                            ry -= 1
        lines = rotate(lines)
    return lines


"""  
P1:
# lines n to s
load = 0
for r, line in enumerate(lines):
    # for each rock, move it forwards until it hits a #, O or the end of the file
    for c, rock in enumerate(line):
        if rock == "O":
            ry, rx = r, c
            while True:
                # if the square N of the rock is a hash or EoF
                if ry-1 < 0:
                    load += len(lines) - ry
                    break
                elif lines[ry-1][rx] == "#":
                    load += len(lines) - ry
                    break
                elif lines[ry-1][rx] == "O":
                    load += len(lines) - ry
                    break
                else:
                    lines[ry-1][rx] = "O"
                    lines[ry][rx] = "."
                    ry -= 1
"""
## P2 ##
iteration_repeated = None
SEEN = []
SEEN.append(lines)
for i in range(1, 200000):
    print(i) if i % 1000 == 0 else None
    curr = cycle(deepcopy(SEEN[-1]))
    if curr in SEEN:
        iteration_repeated = i
        iteration_before = SEEN.index(curr)
        print(iteration_before, iteration_repeated)
        break
    else:
        SEEN.append(curr)
        #display(SEEN[-1])

repeats_every = iteration_repeated - iteration_before

curr = SEEN[iteration_before+((1000000000-iteration_before) % repeats_every)]
print(iteration_before+((1000000000-iteration_before) % repeats_every))


# display(curr)
load = 0
for r in range(len(curr)):
    for c in range(len(curr[0])):
        if curr[r][c] == "O":
            load += len(curr) - r
print(load)
