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
# infile = "example.in"
p1 = 0
p2 = 0
D = list(map(int, open(infile).read().strip().split(" ")))
recursion_depth = 0

@functools.cache
def recBlinkNum(n, recursion_depth) -> int:
    # print(len(cached_results), recursion_depth)
    # Base Case:
    if recursion_depth == 75:
        return 1
    # recursive case
    recursion_depth += 1
    if n == 0:
        return recBlinkNum(1, recursion_depth)
    elif len(str(n)) % 2 == 0:
        s = str(n)
        mid = len(s) // 2
        nStone = (int(s[:mid]))
        nStone1 = (int(s[mid:]))
        return recBlinkNum(nStone, recursion_depth) + recBlinkNum(nStone1, recursion_depth)

    else:
        return recBlinkNum(n*2024, recursion_depth)


start = time.time()


pr(sum(recBlinkNum(rock, 0) for rock in D))

print((time.time() - start)*10**3)