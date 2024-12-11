import sys
import re
from collections import defaultdict, Counter, deque
import pyperclip as pc


def pr(s):
    print(s)
    pc.copy(s)


sys.setrecursionlimit(10**6)
infile = "input.in"
# infile = "example.in"
p1 = 0
p2 = 0
D = open(infile).read().strip().split("\n")


def doRecursive(subTotal, target, l, *ops):
    # print(f"{subTotal=}, {target=}, {l=}")
    # base case
    if len(l) == 0:
        if subTotal == target:
            return True
        else:
            return False
    # recursive case
    else:
        if subTotal <= target:
            for i in range(len(ops)):
                if doRecursive(ops[i](subTotal, l[0]), target, l[1:], *ops):
                    return True
        else:
            return False


def concat(e1, e2):
    return int(str(e1) + str(e2))

def mul(e1, e2):
    return int(e1*e2)

def add(e1, e2):
    return int(e1+e2)

for line in D:
    line = line.split(" ")
    target = int(line[0][:-1])
    values = list(map(int, line[1:]))
    if doRecursive(values[0], target, values[1:], mul, add, concat):
        p2 += target

pr(p2)
