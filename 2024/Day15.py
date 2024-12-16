with open("input.in", "r") as f:
    map, instructions = f.read().split("\n\n")
    map = map.split("\n")
    instructions = "".join(instructions.split("\n"))
matrix = []
robot_coords = ()
for r, line in enumerate(map):
    row = []
    for c, char in enumerate(line):
        if char == "@":
            robot_coords = (r, 2*c)
            row.append("@")
            row.append(".")
        elif char == "O":
            row.append("[")
            row.append("]")
        elif char == "#":
            row.append("#")
            row.append("#")
        else:
            row.append(".")
            row.append(".")
    matrix.append(row)


def display(m):
    for out in m:
        row = ""
        for c in out:
            row += c
        print(row)
    print()


def extract_component(map, r, c, dr, dc):
    if map[r][c] in ['#', '.']:
        return []
    ch = map[r][c]
    map[r][c] = '.'
    component = [(r, c, ch)]
    component.extend(extract_component(map, r + dr, c + dc, dr, dc))
    if ch == '[':
        component.extend(extract_component(map, r, c + 1, dr, dc))
    if ch == ']':
        component.extend(extract_component(map, r, c - 1, dr, dc))
    return component


def validate(component, dr, dc):
    for cell in component:
        if matrix[cell[0] + dr][cell[1] + dc] != ".":
            return False
    return True


for ins in instructions:
    # Find the whole component that is being pushed, including the robot cell, and erase it (replacing with '.' on the map).
    if ins == "<":
        dr = 0
        dc = -1
    elif ins == ">":
        dr = 0
        dc = 1
    elif ins == "^":
        dr = -1
        dc = 0
    elif ins == "v":
        dr = 1
        dc = 0

    component = extract_component(
        matrix, robot_coords[0], robot_coords[1], dr, dc)
    # Check if there is an empty cell in the moving direction for all cells in the component.
    willMove = validate(component, dr, dc)

    # If so, move all the cells in the given direction.
    if willMove:
        movedComp = []
        for cell in component:
            newcell = (cell[0] + dr, cell[1] + dc, cell[2])
            movedComp.append(newcell)
        component = movedComp
        robot_coords = (robot_coords[0] + dr, robot_coords[1] + dc)

    # Put the cells (that may or may not have moved) back onto the map.
    for cell in component:
        matrix[cell[0]][cell[1]] = cell[2]

p1 = 0
for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if char == "[":
            p1 += r * 100 + c
display(matrix)
print(p1)
