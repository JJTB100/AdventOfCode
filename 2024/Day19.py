import re
import sys
import functools
import time
sys.setrecursionlimit(10**6)

with open("input.in", "r") as f:
    patterns, towels = f.read().split("\n\n")

patterns = patterns.split(", ")
towels = towels.split("\n")

patterns.sort(key=lambda t: (-len(t), t))


strt = time.time()


@functools.cache
def howManyComb(towel):
    if towel == "":
        return True
    else:
        count = 0
        for pattern in patterns:
            if towel.startswith(pattern):
                count += howManyComb(towel[len(pattern):])
        return count


total = 0
count = 0
for towel in towels:
    this_towel = howManyComb(towel)
    count += 1 if this_towel > 0 else 0
    total += this_towel
print(count)
print(total)


print(time.time()-strt)
