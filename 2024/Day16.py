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
        def __init__(self, y, x, working_value=10000000000000000000, dir=None):
            self.y = y
            self.x = x
            self.working_value = working_value
            self.dir = dir
            self.prev = []

        def __eq__(self, other):
            return self.y == other.y and self.x == other.x

        def __hash__(self):
            return hash((self.y, self.x))

    ## Create unvisited set ##
    unvisited = []
    visited = []
    unvisited.append(node(start[0], start[1], working_value=0, dir=1))
    adjs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    ## While we've not seen everything ##
    while len(unvisited) != 0:
        sorted(unvisited, key=lambda x: x.working_value)
        current = unvisited.pop(0)
        if current.y == end[0] and current.x == end[1]:
            end_node = current
        else:
            ## Consider all of current's unvisited neighbours ##
            for i in range(0, 3):
                dy, dx = adjs[i]

                neighbour = node(current.y + dy, current.x +
                                 dx, dir=i)
                if neighbour in visited:
                    neighbour = visited[visited.index(neighbour)]
                    neighbour.dir = i

                if not (current.x == start[1] and current.y == start[0]) and neighbour in current.prev:
                    continue
                if matrix[neighbour.y][neighbour.x] == "#":
                    continue

                else:
                    if int(current.dir) != int(neighbour.dir):
                        possible_new_value = current.working_value + 1001
                    else:
                        possible_new_value = current.working_value + 1

                    if int(possible_new_value) < int(neighbour.working_value):
                        neighbour.working_value = possible_new_value
                        neighbour.prev = [current]
                        unvisited.append(neighbour)
                        visited.append(neighbour)
                        print(current.y, current.x, neighbour.working_value)
                    elif int(possible_new_value) == int(neighbour.working_value) or int(possible_new_value) == int(neighbour.working_value-1000) or int(possible_new_value) == int(neighbour.working_value+1000):
                        neighbour.prev.append(current)
                        unvisited.append(neighbour)
                        visited.append(neighbour)
                        print(current.y, current.x, neighbour.working_value, "EQUAL")

    print("P1:", end_node.working_value)

   ## need to return the list of coords that are part of the path ##
   ## backtrack through visited, if there are two options, go back through both ##

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
dots = findAll(matrix, ".")
end_coords = findAll(matrix, "E").pop()
start_coords = findAll(matrix, "S").pop()

## Do Dijkstra's Algorithm to find the shortest path ##
paths = Dijkstra(start_coords, end_coords)

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

print(len(set(paths)))
