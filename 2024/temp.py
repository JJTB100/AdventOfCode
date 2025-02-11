import re
import sys
import functools
import time
sys.setrecursionlimit(10**6)

with open("input.in", "r") as f:
    towels, designs = f.read().split("\n\n")

towels = towels.split(", ")
designs = designs.split("\n")

towels.sort(key=lambda t: (-len(t), t))

strt = time.time()

@functools.cache
def ways(s: str) -> int:
    return sum(s.startswith(t) and (len(s) == len(t) or ways(s[len(t):])) for t in towels)


patterns = list(ways(design) for design in designs)
print(f"Possible designs: {sum(n > 0 for n in patterns)}")
print(f"Possible ways: {sum(patterns)}")


print(time.time()-strt)
