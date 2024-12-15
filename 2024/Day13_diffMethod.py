import time
import pyperclip as pc
import functools
from collections import defaultdict, Counter, deque
import re
import sys
import numpy as np
import sympy as sym


def pr(s):
    print(s)
    pc.copy(s)


start = time.time()
def is_int(i):
    try: sym.as_int(i, strict=False)
    except: return False
    return True

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
                    (m[4]+10000000000000, m[5]+10000000000000)])

for machine in machines:
    A, B, P = machine[0], machine[1], machine[2]
    # solve simultaneous equations
    a, b = sym.symbols('a, b')
    eq1 = sym.Eq(a*A[0] + b*B[0], P[0])             # x + y + z  = 1
    eq2 = sym.Eq(a*A[1] + b*B[1], P[1])         # x + y + 2z = 3
    sol = sym.solve((eq1, eq2), (a, b))
    if sym.Float(sol[a])%1==0 and sym.Float(sol[b])%1==0:
        p1 += sol[a]*3+sol[b]
    


pr(int(p1))
print((time.time() - start)*10**3)
