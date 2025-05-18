""" Advent Of Code 2019 : 3 """

from aoctools import *

def manhattanDistance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def main(aocd: AOCD):

    lines = aocd.slist_split_at("\n")
    lines = [list(map(lambda x: (x[0], int(x[1:])), line.split(","))) for line in lines]
    line_coords = [{}, {}]
    for i in range(2):
        head = (0, 0) # (y,x)
        steps = 0
        for instruction in lines[i]:
            match instruction[0]:
                case "U":
                    for _ in range(instruction[1]):
                        steps += 1
                        head = (head[0] - 1, head[1])
                        line_coords[i][head] = steps
                case "D":
                    for _ in range(instruction[1]):
                        steps += 1
                        head = (head[0] + 1, head[1])
                        line_coords[i][head] = steps
                case "L":
                    for _ in range(instruction[1]):
                        steps += 1
                        head = (head[0], head[1]-1)
                        line_coords[i][head] = steps
                case "R":
                    for _ in range(instruction[1]):
                        steps += 1
                        head = (head[0], head[1]+1)
                        line_coords[i][head] = steps
    intersections = {}
    for coord in line_coords[0]:
        if coord in line_coords[1]:
            intersections[coord] = line_coords[0][coord] + line_coords[1][coord]
    print(intersections)
    aocd.p1(manhattanDistance((0,0), sorted(list(intersections.items()), key=lambda x: manhattanDistance((0,0), x[0]))[0][0]))
    aocd.p2(min(intersections.values()))



if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2019, 3)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
