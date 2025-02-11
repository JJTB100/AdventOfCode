import sys
sys.setrecursionlimit(10**6)


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


def Dijkstra(start, end):
    class node:
        def __init__(self, y, x, dir, working_value=10000000000000000000):
            self.y = y
            self.x = x
            self.working_value = working_value
            self.dir = dir
            self.prev = []

        def __eq__(self, other):
            return self.y == other.y and self.x == other.x and self.dir == other.dir

        def __str__(self):
            return f"({self.y}, {self.x}, {self.dir}, {self.working_value})"

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
    # Push with priority
    unvisited.append(node(start[0], start[1], 1, working_value=0))

    adjs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while len(unvisited) != 0:
        unvisited.sort(key=lambda x: x.working_value)
        current = unvisited.pop(0)
        """
        print(f"{current}  ", end="")
        for n in unvisited:
            print(f"{n}", end="")
        print()
        """

        for i in range(4):
            dy, dx = adjs[i]

            if (current.dir + 2) % 4 == i:
                continue

            if matrix[current.y + dy][current.x + dx] == "#":
                continue

            neighbour = visited.get(
                (current.y + dy, current.x + dx, i), node(-1, -1, -1))
            if neighbour.y == -1:
                neighbour = node(current.y + dy, current.x + dx, i)
                visited[(neighbour.y, neighbour.x,
                         neighbour.dir)] = neighbour

                # If we've changed direction
            if current.dir != neighbour.dir:
                possible_new_value = current.working_value + 1001
            else:
                possible_new_value = current.working_value + 1

            # If we should replace the working value
            if possible_new_value < neighbour.working_value:
                neighbour.working_value = possible_new_value
                neighbour.prev = [current]
                unvisited.append(
                    neighbour) if not neighbour in unvisited else 0

            # P2: if we meet a path that has identical length
            elif possible_new_value == neighbour.working_value:
                neighbour.prev.append(current)

    end_node = min((visited[(end[0], end[1], k)]
                   for k in range(4) if (end[0], end[1], k) in visited), key=lambda x: x.working_value)
    print("P1:", end_node.working_value)

    return backTrackBFS(end_node)


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

## Do Dijkstra's Algorithm to find the shortest path ##
paths = Dijkstra(start_coords, end_coords)

p2 = 0
for y in range(len(matrix)):
    for x in range(len(matrix[0])):
        contains = False
        for el in paths:
            if el.y == y and el.x == x:
                contains = True
        if contains:
            p2 += 1
            print("O", end="")
        else:
            print(".", end="")
    print()

print("P2:", p2)
