import numpy as np
import itertools
lines = open("input.txt").readlines()
# https://www.desmos.com/3d/9g7qdyprjh


def line_intersection(line1, line2):
    m1 = (line1[1][1]/line1[1][0])
    c1 = line1[0][1] - m1 * line1[0][0]
    m2 = (line2[1][1]/line2[1][0])
    c2 = line2[0][1] - m2 * line2[0][0]
    if m1 == m2:
        print(f"""Hailstone A: {line1}
Hailstone B: {line2}
Hailstones' paths are parallel they never intersect.""")
        return False, None
    else:
        X = (c2 - c1)/(m1 - m2)
        Y = m1 * X + c1
        if not (((line1[1][0] >= 0) == (X >= line1[0][0])) and ((line1[1][1] >= 0) == (Y >= line1[0][1]))):
            print(f"""Hailstone A: {line1}
Hailstone B: {line2}
Hailstones' paths crossed in the past for hailstone A.""")
            return False, None
        if not (((line2[1][0] >= 0) == (X >= line2[0][0])) and ((line2[1][1] >= 0) == (Y >= line2[0][1]))):
            print(f"""Hailstone A: {line1}
Hailstone B: {line2}
Hailstones' paths crossed in the past for hailstone B.""")
            return False, None
        return True, (X, Y)


total = 0
min, max = np.array([200000000000000]), np.array([400000000000000])

combs = itertools.combinations(lines, 2)
for comb in combs:
    pline1, pline2 = comb[0], comb[1]
    if pline1 != pline2:
        line1p = np.array(
            tuple(map(int, pline1.split("@")[0].split(", ")))[:-1])
        line1v = np.array(
            tuple(map(int, pline1.split("@")[1].split(", ")))[:-1])
        line2p = np.array(
            tuple(map(int, pline2.split("@")[0].split(", ")))[:-1])
        line2v = np.array(
            tuple(map(int, pline2.split("@")[1].split(", ")))[:-1])

        line1 = (line1p, line1v)
        line2 = (line2p, line2v)

        intersects, point = line_intersection(line1, line2)

        if intersects:
            if min <= point[0] <= max and min <= point[1] <= max:
                print(point)
                total += 1
print(total)
