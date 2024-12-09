from itertools import combinations
import math


def ParseInput():
    with (open("2023/input.txt", "r") as f):
        lines = f.read().splitlines()

    matrix = []
    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            row.append(char)
        matrix.append(row)
    return matrix


def transpose(l1):
    l2 = []
    # iterate over list l1 to the length of an item
    for i in range(len(l1[0])):
        # print(i)
        row = []
        for item in l1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        l2.append(row)
    return l2


def ApplyGravity(matrix):
    new = []
    # for each row, if no #, add empty row below
    for row in matrix:
        if not "#" in row:
            empty_row = list("n"*len(row))
            new.append(empty_row)
        else:
            new.append(row)

    # for each col, if no #, add empty col right
    Tnew = transpose(new)
    Tout = []
    for row in Tnew:
        if not "#" in row:
            empty_row = list("n"*len(row))
            Tout.append(empty_row)
        else:
            Tout.append(row)

    return transpose(Tout)


def display(matrix):
    for r in range(len(matrix)):
        row = ""
        for c in range(len(matrix[0])):
            row += matrix[r][c]
        print(row)

    print("\n")


def getGalaxies(matrix):
    galaxies = set()
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            galaxies.add((y, x)) if matrix[y][x] == "#" else None
    return galaxies


def shortest_path(start, end, matrix):
    # count the number of ns
    num_of_ns = 0
    if start[1] > end[1]:
        for el in matrix[start[0]][end[1]:start[1]]:
            if el == "n":
                num_of_ns += 1
    else:
        for el in matrix[start[0]][start[1]:end[1]]:
            if el == "n":
                num_of_ns += 1
    lenX = abs(start[1] - end[1]) + num_of_ns * 999999
    num_of_ns = 0
    Tm = transpose(matrix)
    if start[0] > end[0]:
        for el in Tm[start[1]][end[0]:start[0]]:
            if el == "n":
                num_of_ns += 1
    else:
        for el in Tm[start[1]][start[0]:end[0]]:
            if el == "n":
                num_of_ns += 1
    lenY = abs(start[0] - end[0]) + num_of_ns * 999999
    return lenY+lenX


matrix = ParseInput()
matrix = ApplyGravity(matrix)
galaxies = getGalaxies(matrix)
total = 0
i = 0
combs = set(combinations(galaxies, 2))
l = len(combs)
for c1, c2 in combs:
    print(f"{i}/{l}") if i % 1000 == 0 else None
    total += shortest_path(c1, c2, matrix)
    i += 1
print(total)
