from functools import cache 

with open("input.in") as f:
    lines = f.readlines()

graph = {}
for node in lines:
    name, edges = node.strip().split(": ")
    edges = set(edges.split(" "))
    graph[name] = edges
    

@cache
def count_paths_p2(node:str, hasVisistedDAC, hasVisitedFFT) -> int:
    # Base Case
    if node == "out" and hasVisistedDAC and hasVisitedFFT:
        return 1
    elif node == "out":
        return 0
    
    if node == "fft":
        hasVisitedFFT = True
    if node == "dac":
        hasVisistedDAC = True
    # Recursive Case
    return sum(count_paths_p2(child, hasVisistedDAC, hasVisitedFFT) for child in graph[node])

@cache
def count_paths_p1(node:str) -> int:
    # Base Case
    if node == "out":
        return 1
    # Recursive Case
    return sum(count_paths_p1(child) for child in graph[node])

print(count_paths_p1("you"))
print(count_paths_p2("svr", False, False))