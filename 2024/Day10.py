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


def solve(p2=False):
    heads = set()
    # Find 0s
    for r, line in enumerate(D):
        for c, char in enumerate(line):
            if char == "0":
                heads.add((r, c))
    # Q
    end = []
    for h in heads:
        q = []
        h = (h[0], h[1])
        q.append(h)
        # Start a queue wait till it runs out
        while len(q) != 0:
            curr = q.pop(0)
            if D[curr[0]][curr[1]] == "9":
                end.append(curr)
            # Look at surrounding sqrs
            adj = [(y+curr[0], x+curr[1]) for (y, x) in {(-1, 0), (1, 0), (0, 1), (0, -1)}
                   if 0 <= y+curr[0] < len(D) if 0 <= x+curr[1] < len(D[0]) and D[y+curr[0]][x+curr[1]] != "."]
            # add each sqr where diff is 1 to curr
            for a in adj:
                if int(D[a[0]][a[1]]) - int(D[curr[0]][curr[1]]) == 1:
                    if p2:
                        q.append(a)
                    else:
                        if not a in q:
                            q.append(a)
    return len(end)


p1 = solve()
p2 = solve(True)
pr(p1)
pr(p2)
