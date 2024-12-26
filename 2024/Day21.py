import os
from pathlib import Path
from itertools import product
from collections import Counter

DIRECTIONS = [(-1, 0), (0, 1),
              (1, 0), (0, -1)]
UP, RIGHT, DOWN, LEFT = DIRECTIONS
def add(*ps): return tuple(map(sum, zip(*ps)))


def sub(p1, p2):
    return tuple(a-b for a, b in zip(p1, p2))



with open("input.in") as file:
    lines = file.read().splitlines()
    
num_pad_lines = """
789
456
123
.0A
""".strip().splitlines()

dir_pad_lines = """
.^A
<v>
""".strip().splitlines()

num_pad = {(i, j): c for i, line in enumerate(num_pad_lines)
           for j, c in enumerate(line) if c != "."}
dir_pad = {(i, j): c for i, line in enumerate(dir_pad_lines)
           for j, c in enumerate(line) if c != "."}

num_pad.update({v: k for k, v in num_pad.items()})
dir_pad.update({v: k for k, v in dir_pad.items()})

def step(source, target, pad):
    target_i, target_j = pad[target]
    source_i, source_j = pad[source]
    di = target_i - source_i
    dj = target_j - source_j
    
    ## Check if it goes off the path:
    vert = "v"*di+"^"*-di
    horiz = ">"*dj+"<"*-dj
    if dj > 0 and (target_i, source_j) in pad:
        return vert+horiz+"A"
    if (source_i, target_j) in pad:
        return horiz+vert+"A"
    if (target_i, source_j) in pad:
        return vert+horiz+"A"


def routes(path, pad):
    out = []
    start = "A"
    for end in path:
        out.append(step(start, end, pad))
        start = end
    return "".join(out)


num_routes = [routes(line, num_pad) for line in lines]
rad_routes = [routes(route, dir_pad) for route in num_routes]
cold_routes = [routes(route, dir_pad) for route in rad_routes]
p1 = sum(len(route) * int(line[:-1]) for route, line in zip(cold_routes, lines))
print("Part 1:", p1)


def routes2(path, pad):
    out = []
    start = "A"
    for end in path:
        out.append(step(start, end, pad))
        start = end
    return Counter(out)


def route_len(route):
    return sum(len(k)*v for k, v in route.items())


robot_routes = [Counter([route]) for route in num_routes]
for _ in range(25):
    new_routes = []
    for route_counter in robot_routes:
        new_route = Counter()
        for sub_route, qty in route_counter.items():
            new_counts = routes2(sub_route, dir_pad)
            for k in new_counts:
                new_counts[k] *= qty
            new_route.update(new_counts)
        new_routes.append(new_route)
    robot_routes = new_routes

p2 = sum(route_len(route)*int(line[:-1])
         for route, line in zip(robot_routes, lines))
print("Part 2:", p2)
