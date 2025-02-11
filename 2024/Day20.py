import time
import itertools


def findAll(matrix: list[list[str]], chars: str):
    """
    Finds all chars in matrix

    Arguments:
    Chars, the characters to find (can be a string)
    matrix, the matrix to find in

    Returns:
    a set of coordinates containing every occurance of (many) chars
    """
    pos = set()
    for y, row in enumerate(matrix):
        for x, c in enumerate(row):
            if c in chars:
                pos.add((y, x))
    return pos


def display(paths):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            contains = False
            if (y, x) in paths:
                print(".", end="")
            elif (y, x) in base_path:
                print("O", end="")
            else:
                print("*", end="")

        print()
    print()


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
            paths.append((curr.y, curr.x))
            ## look at each of the curr's prev ##
            prev_nodes = curr.prev
            if prev_nodes == None:
                continue
            for prev in prev_nodes:
                Q.append(prev)
        return paths

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
                (current.y + dy, current.x + dx), node(-1, -1))
            if neighbour.y == -1:
                neighbour = node(current.y + dy, current.x + dx)
                visited[(neighbour.y, neighbour.x)] = neighbour

            if neighbour.visited:
                continue

            possible_new_value = current.working_value + 1

            # If we should replace the working value
            if possible_new_value < neighbour.working_value:
                neighbour.working_value = possible_new_value
                neighbour.prev = [current]
                unvisited.append(
                    neighbour)
    try:
        end_node = visited[(end[0], end[1])]
        return backTrackBFS(end_node)
    except KeyError:
        return None


## Parse input ##
with open("input.in", "r") as f:
    lines = f.read().splitlines()
    matrix = []
    for line in lines:
        row = []
        for c in line:
            row.append(c)
        matrix.append(row)

## Get coords of important features ##
end_coords = findAll(matrix, "E").pop()
start_coords = findAll(matrix, "S").pop()

base_path = Dijkstra(start_coords, end_coords)

# Get each soft wall in matrix
soft_walls = []
for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if char == "#":
            if 0 < c < len(row)-1 and 0 < r < len(matrix)-1:
                if ((r-1, c) in base_path and (r+1, c) in base_path) or ((r, c-1) in base_path and (r, c+1) in base_path):
                    soft_walls.append((r, c))


count = 0
for n, wall in enumerate(soft_walls):
    wall_neighbours = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in dirs:
        i2 = wall[0] + di
        j2 = wall[1] + dj
        if i2 >= 0 and j2 >= 0 and i2 < len(matrix) and j2 < len(matrix[0]) and (i2, j2) in base_path:
            wall_neighbours.append((i2, j2))

    ps = [base_path.index(p) for p in wall_neighbours]
    time_saved = max(ps) - min(ps) - 2

    if time_saved >= 100:
        count += 1

print(count)
start = time.time()
p2 = 0
i = 0
lenCombs = 43772046

for sqr1, sqr2 in itertools.combinations(base_path, 2):
    if abs(sqr1[1] - sqr2[1]) + abs(sqr1[0] - sqr2[0]) <= 20:
        ps = [base_path.index(p) for p in [sqr1, sqr2]]
        time_saved = max(ps) - min(ps) - \
            (abs(sqr1[1] - sqr2[1]) + abs(sqr1[0] - sqr2[0]))
        if time_saved >= 100:
            p2 += 1
    print(f"{i}/{lenCombs} | {i/lenCombs*100:3f}%") if i % 100020 == 0 else 0
    i += 1

print(p2)

print(f"{time.time() - start}s")
