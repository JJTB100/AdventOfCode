import time
import pyperclip as pc
import functools
from collections import defaultdict, Counter, deque
import re
import sys
import numpy as np


def pr(s):
    print(s)
    pc.copy(s)


start = time.time()

sys.setrecursionlimit(10**6)
infile = "input.in"
# infile = "example.in"

p1 = 0
p2 = 0
machines1 = open(infile).read()
machines = []
for m in re.findall(r"X\+(\d+), Y\+(\d+)\r?\n.+X\+(\d+), Y\+(\d+)\r?\n.+X\=(\d+), Y\=(\d+)", machines1):
    m = list(map(int, m))
    machines.append([(m[0], m[1]), (m[2], m[3]),
                    (m[4]+10000000000000, m[5]+10000000000000)]) # p2

for machine in machines:
    A, B, P = machine[0], machine[1], machine[2]
    # solve simultaneous equations
    mat1 = np.array([[A[0], B[0]], [A[1], B[1]]], dtype=np.float64)
    solution = np.array(list(P), dtype=np.float64)
    sol = np.linalg.solve(mat1, solution)

    if round(sol[0], 2).is_integer() and round(sol[1], 2).is_integer():
        p1 += sol[0]*3+sol[1]

pr(int(p1))
print((time.time() - start)*10**3)
