import sys
import re
from collections import defaultdict, Counter, deque
import functools
import pyperclip as pc
import time


def pr(s):
    print(s)
    pc.copy(s)


sys.setrecursionlimit(10**6)
infile = "input.in"
infile = "example.in"

start = time.time()


p1 = 0
p2 = 0
maps = list(open(infile).read().strip().split("\n\n"))


def findReflection(m) -> int:
    # for each indice in m
    i = 0
    while i < len(m)-1:
        # if there's a reflection after i
        if isReflection(i, m):
            return i
        i += 1
    return None


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
        l2.append("".join(row))
    return l2


def isReflection(i, m):
    j = i + 1
    while 0 <= i and j < len(m):
        if m[i] == m[j]:
            i -= 1
            j += 1
            continue
        else:
            return False
    return True


def getReflectionDiff(i, m):
    j = i + 1
    while 0 <= i and j < len(m):
        diffs = []
        for k in range(len(m[0])):
            if m[i][k] != m[j][k]:
                if len(diffs) > 1:
                    break
                else:
                    diffs.append(k)
        if len(diffs) == 1:
            return (i, diffs[0])
        i -= 1
        j += 1
    return None


def findDiffRef(m):
    # for each indice in m
    i = 0
    while i < len(m)-1:
        # if there's a reflection diff of 1 after i
        k = getReflectionDiff(i, m)
        if k != None:
            return k
        i += 1
    return None


def solvep1(m):
    vertical_after = findReflection(transpose(m))
    horizontal_after = findReflection(m)
    return (vertical_after+1) if vertical_after != None else 100*(horizontal_after+1) if horizontal_after != None else -1


def solvep2(m):
    v_diff = findDiffRef(transpose(m))
    h_diff = findDiffRef(m)
    print(f"v_diff: {v_diff}, h_diff: {h_diff}")
    (y, x) = v_diff if v_diff != None else h_diff
    if m[y][x] == ".":
        m[y] = m[y][:x] + "#" + m[y][x+1:]
    elif m[y][x] == "#":
        m[y] = m[y][:x] + "." + m[y][x+1:]

    return solvep1(m)


for m in maps:
    m = m.split("\n")
    k = solvep1(m)
    l = solvep2(m)
    p1 += k
    p2 += l


pr(p1)
pr(p2)
