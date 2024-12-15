import time
import pyperclip as pc
import functools
from collections import defaultdict, Counter, deque
import re
import sys
import numpy as np
from math import floor


def prRed(skk, end="\n"): print(f"\033[91m{skk}\033[00m", end=end)


def prGreen(skk, end="\n"): print(f"\033[92m{skk}\033[00m", end=end)


def prYellow(skk, end="\n"): print(f"\033[93m{skk}\033[00m", end=end)


def prLightPurple(skk, end="\n"): print(f"\033[94m{skk}\033[00m", end=end)


def prPurple(skk, end="\n"): print(f"\033[95m{skk}\033[00m", end=end)


def prCyan(skk, end="\n"): print(f"\033[96m{skk}\033[00m", end=end)


def prLightGray(skk, end="\n"): print(f"\033[97m{skk}\033[00m", end=end)


def prBlack(skk, end="\n"): print(f"\033[98m{skk}\033[00m", end=end)


def pr(s):
    print(s)
    pc.copy(s)


start = time.time()

sys.setrecursionlimit(10**6)
infile = "input.in"
# infile = "example.in"

p1 = 0
p2 = 0
robots = []  # [[(pos),(vel)],]
MAXY = 103
MAXX = 101
with open(infile, "r") as f:
    lines = f.readlines()
for line in lines:
    x, y, vx, vy = re.findall(
        r"^p=(.?\d+),(.?\d+) v=(.?\d+),(.?\d+)$", line)[0]
    robots.append([(int(y), int(x)), (int(vy), int(vx))])


def simulate(pos, vel, secs=100) -> tuple:
    newpos = (pos[0]+secs*(vel[0]), pos[1]+secs*(vel[1]))
    while newpos[0] >= MAXY:
        newpos = (newpos[0]-MAXY, newpos[1])
    while newpos[1] >= MAXX:
        newpos = (newpos[0], newpos[1]-MAXX)
    while newpos[0] < 0:
        newpos = (newpos[0]+MAXY, newpos[1])
    while newpos[1] < 0:
        newpos = (newpos[0], newpos[1]+MAXX)
    return newpos


def display(robots):
    empty_row = [0 for _ in range(MAXX)]
    output = []
    for _ in range(MAXY):
        output.append(empty_row.copy())
    for robot in robots:
        output[robot[0][0]][robot[0][1]] = output[robot[0][0]][robot[0][1]] + 1

    for out in output:
        for c in out:
            if c == 0:
                print(" ", end="")
            else:
                print(c, end="")
        print()


lowest = 100000000000000
for i in range(1, 10000):
    first_quad = []
    second_quad = []
    third_quad = []
    fourth_quad = []
    for robot in robots:
        robot[0] = simulate(robot[0], robot[1], 1)

    for robot in robots:
        if robot[0][0] < floor(MAXY/2) and robot[0][1] < floor(MAXX/2):
            first_quad.append(robot)
        elif robot[0][0] < floor(MAXY/2) and robot[0][1] > floor(MAXX/2):
            second_quad.append(robot)
        elif robot[0][0] > floor(MAXY/2) and robot[0][1] < floor(MAXX/2):
            third_quad.append(robot)
        elif robot[0][0] > floor(MAXY/2) and robot[0][1] > floor(MAXX/2):
            fourth_quad.append(robot)
    safety_fac = len(first_quad) * len(second_quad) * \
        len(third_quad) * len(fourth_quad)
    if safety_fac < lowest:
        print(f"{i}:")
        display(robots)
        lowest = safety_fac


p1 = len(first_quad) * len(second_quad) * len(third_quad) * len(fourth_quad)

pr(p1)
print((time.time() - start)*10**3)
