from itertools import combinations
import math

with open("input.in") as f:
    lines = f.readlines()

coords = []
for line in lines:
    coords.append(tuple(int(c) for c in line.strip().split(",")))

## Implementation of Kruskal's, running for 10(00) connections
forest = []
for coord in coords:    
    forest.append(set(((coord),)))
edges = {}
for v1, v2 in combinations(coords,2):
    edges[(v1, v2)] = (v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2

def find_set(u):
    for s in forest:
        if u in s:
            return s

print(forest)

connections = 0
for k, edge in sorted(edges.items(), key=lambda x: x[1]):
    u,v = k[0], k[1]
    setU = find_set(u)
    setV = find_set(v)
    if setU != setV:
        forest.remove(setU)
        forest.remove(setV)
        union = set.union(setU, setV)
        forest.append(union)
        print(f"Connect {connections}:", u, v, edge)
        print(f"  {len(union)}     {union}")
    connections += 1
    if len(forest) == 1: 
        p2 = u[0] * v[0]
        break
for s in forest:
    print(f"{len(s)}: {s}")

print(p2)