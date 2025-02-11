import time
import re
import sys
sys.setrecursionlimit(10**6)


def Dijkstra(start, end):
    class node:
        def __init__(self, y, x, working_value=10000000000000000000):
            self.y = y
            self.x = x
            self.working_value = working_value
            self.prev = []
            self.visited = False

        def __eq__(self, other):
            return self.y == other.y and self.x == other.x

        def __str__(self):
            return f"({self.y}, {self.x}, {self.working_value})"

    def backTrackBFS(end_node) -> int:
        paths = []
        Q = []
        Q.append(end_node)
        while len(Q) != 0:
            curr = Q.pop(0)
            paths.append(curr)
            ## look at each of the curr's prev ##
            prev_nodes = curr.prev
            if prev_nodes == None:
                continue
            for prev in prev_nodes:
                Q.append(prev)
        return paths

    def display(current):
        paths = backTrackBFS(current)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                contains = False
                for el in paths:
                    if el.y == y and el.x == x:
                        contains = True
                if contains:
                    print("O", end="")
                else:
                    print(".", end="")
            print()
        print()

    unvisited = []
    visited = {}

    unvisited.append(node(start[0], start[1], working_value=0))

    adjs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while len(unvisited) != 0:

        current = unvisited.pop(0)
        current.visited = True
        for i in range(4):
            dy, dx = adjs[i]

            if not (0 <= current.y + dy < len(matrix) and 0 <= current.x + dx < len(matrix[0])):
                continue

            if matrix[current.y + dy][current.x + dx] == "#":
                continue

            neighbour = visited.get(
                (current.y + dy, current.x + dx), node(-1, -1, -1))
            if neighbour.y == -1:
                neighbour = node(current.y + dy, current.x + dx)
                visited[(neighbour.y, neighbour.x)] = neighbour

            if neighbour.visited:
                continue

            heuristic = ((neighbour.y - end[0]) **
                         2+(neighbour.x - end[1])**2)**(1/2)

            possible_new_value = current.working_value + 1 + heuristic

            # If we should replace the working value
            if possible_new_value < neighbour.working_value:
                neighbour.working_value = possible_new_value
                neighbour.prev = [current]
                unvisited.append(
                    neighbour)

            if neighbour.x == end[1] and neighbour.y == end[0]:
                return neighbour.working_value

    try:
        end_node = visited[(end[0], end[1])]
        return end_node.working_value
    except KeyError:
        return None


## Parse input ##
with open("input.in", "r") as f:
    lines = f.read().splitlines()
    lines = list(list(map(int, line.split(","))) for line in lines)
    firstKB = lines[:1025]
    matrix = []
    for y in range(0, 71):
        row = []
        for x in range(0, 71):
            if [x, y] in firstKB:
                row.append("#")
            else:
                row.append(".")
        matrix.append(row)


## Get coords of important features ##
end_coords = (70, 70)
start_coords = (0, 0)
startTIME = time.time()
for i in range(1025, len(lines)):
    matrix[lines[i][1]][lines[i][0]] = "#"
    ## Do Dijkstra's Algorithm to find the shortest path ##
    path_len = Dijkstra(start_coords, end_coords)

    if path_len == None:
        print(i, f"({lines[i][0]}, {lines[i][1]})")
        break
    # else:
        # print(path_len, "<- Not answer", f"{i-1024} out of {len(lines)-1024}")

print(time.time() - startTIME)
