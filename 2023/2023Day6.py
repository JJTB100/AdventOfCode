import re
import math
with open("input.txt", "r") as f:
    times, distances = f.read().splitlines()

times = list(map(int, re.findall(r"\d+", times)))
distances = list(map(int, re.findall(r"\d+", distances)))

total = 1

t = times[0]
d = distances[0] + 1
minHoldTime = math.floor((t+((t**2)-4*d)**(1/2))/2)
maxHoldTime = math.ceil((t-((t ** 2)-4*d)**(1/2))/2)

total *= (minHoldTime - maxHoldTime + 1)

print(total)
