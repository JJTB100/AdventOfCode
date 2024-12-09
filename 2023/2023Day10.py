import sys
sys.setrecursionlimit(70000)
with (open("input.txt", "r") as f):
    lines = f.read().splitlines()
# Parse input, find S
matrix = []
s_coords = ()
for y, line in enumerate(lines):
    row = []
    for x, char in enumerate(line):
        if char == "S":
            s_coords = (y, x)
        row.append(char)
    matrix.append(row)


def findMiddle(input):
    middle_pos = int(((len(input) + 1) / 2) - 1)
    return middle_pos


def visit(y, x):
    # base case
    if matrix[y][x] == "S":
        return None
    else:
        # print(matrix[y][x])
        match matrix[y][x]:
            # | is a vertical pipe connecting north and south.
            case "|":
                if visited[-2][0] < y:  # means we've come from the top
                    visited.append((y+1, x))
                    visit(y+1, x)
                else:
                    visited.append((y-1, x))
                    visit(y-1, x)
            # - is a horizontal pipe connecting east and west.
            case "-":
                if visited[-2][1] < x:  # means we've come from the left
                    visited.append((y, x+1))
                    visit(y, x+1)
                else:
                    visited.append((y, x-1))
                    visit(y, x-1)
            # L is a 90-degree bend connecting north and east.
            case "L":
                if visited[-2][0] < y:  # means we've come from the top
                    visited.append((y, x+1))
                    visit(y, x+1)
                else:
                    visited.append((y-1, x))
                    visit(y-1, x)
            # J is a 90-degree bend connecting north and west.
            case "J":
                if visited[-2][0] < y:  # means we've come from the top
                    visited.append((y, x-1))
                    visit(y, x-1)
                else:
                    visited.append((y-1, x))
                    visit(y-1, x)
            # 7 is a 90-degree bend connecting south and west.
            case "7":
                if visited[-2][1] < x:  # means we've come from the left
                    visited.append((y+1, x))
                    visit(y+1, x)
                else:
                    visited.append((y, x-1))
                    visit(y, x-1)
            # F is a 90-degree bend connecting south and east.
            case "F":
                if visited[-2][1] > x:  # means we've come from the right
                    visited.append((y+1, x))
                    visit(y+1, x)
                else:
                    visited.append((y, x+1))
                    visit(y, x+1)


def find_next_from_S(y, x):
    next = ()
    # left:
    if x != 0 and (matrix[y][x-1] == "L" or matrix[y][x-1] == "-" or matrix[y][x-1] == "F" or matrix[y][x-1] == "S") and (y, x):
        next = (y, x-1)
    # right:
    elif x != len(matrix[0])-1 and (matrix[y][x+1] == "7" or matrix[y][x+1] == "-" or matrix[y][x+1] == "J" or matrix[y][x+1] == "S") and (y, x):
        next = (y, x+1)
    # up:
    elif y != 0 and (matrix[y-1][x] == "|" or matrix[y-1][x] == "7" or matrix[y-1][x] == "F" or matrix[y-1][x] == "S") and (y, x):
        next = (y-1, x)
    # down:
    elif y != len(matrix)-1 and (matrix[y+1][x] == "S" or matrix[y+1][x] == "J" or matrix[y+1][x] == "L" or matrix[y+1][x] == "|") and (y, x):
        next = (y+1, x)
    return next[0], next[1]


visited = []
visited.append(s_coords)
ny, nx = find_next_from_S(s_coords[0], s_coords[1])
visited.append((ny, nx))
visit(ny, nx)

# Part 2:


def double(loop):
    loop2 = []
    for el in loop:
        loop2.append((2*el[0], 2*el[1]))

    connected = []
    for i in range(len(loop2)-1):
        connected.append(loop2[i])
        middleX = int(0.5*(loop2[i+1][1]-loop2[i][1])+loop2[i][1])
        middleY = int(0.5*(loop2[i+1][0]-loop2[i][0])+loop2[i][0])
        connected.append((middleY, middleX))
    connected.append(loop2[-1])
    return connected


def display(loop, gridY, gridX):
    for r in range(gridY):
        row = ""
        for c in range(gridX):
            row += "O" if (r, c) in loop else "."
        print(row)

    print("\n")


def Flood(node, loop, gridY, gridX):
    """
    1.  Set Q to the empty queue or stack.
    2.  Add node to the end of Q.
    3.  While Q is not empty:
    4.  Set n equal to the first element of Q.
    5.  Remove first element from Q. 
    6.  If n is Inside:
            Set the n
            Add the node to the west of n to the end of Q.
            Add the node to the east of n to the end of Q.
            Add the node to the north of n to the end of Q.
            Add the node to the south of n to the end of Q.
    7. Continue looping until Q is exhausted.
    8. Return.
    """
    Q = []
    Q.append(node)
    visited = []
    while len(Q) != 0:
        n = Q[0]
        Q.pop(0)
        if n not in loop and n not in visited and 0 <= n[0] < gridY and 0 <= n[1] < gridX:
            visited.append(n)
            Q.append((n[0]-1, n[1]))
            Q.append((n[0]+1, n[1]))
            Q.append((n[0], n[1]-1))
            Q.append((n[0], n[1]+1))
    return visited


def getEven(coords):
    good = []
    for i in range(len(coords)):
        if coords[i][0] % 2 == 0 and coords[i][1] % 2 == 0:
            good.append(coords[i])
    return good


loop = visited.copy()
double_loop = double(loop)

gridY = len(lines)*2 + 2
gridX = len(lines[0])*2 + 2
start = (0, 0)

for i in range(len(double_loop)):
    double_loop[i] = (double_loop[i][0]+1, double_loop[i][1]+1)
# display(double_loop, gridY, gridX)


outside = Flood(start, double_loop, gridY, gridX)
# display(outside, gridY, gridX)
everything = {(i, j) for i in range(gridY)
              for j in range(gridX)}
inside = (list(everything - set(outside) - set(double_loop)))
# display(inside, gridY, gridX)


for i in range(len(inside)):
    inside[i] = (inside[i][0]-1, inside[i][1]-1)
inside = getEven(inside)

# ANSWER:
print(len(inside))
