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


display(matrix)
for ins in instructions:
    print(robot_coords)
    print(ins, ":")
    Move(ins)
    display(matrix)

p1 = 0
for r, row in enumerate(matrix):
    for c, char in enumerate(row):
        if char == "O":
            p1 += r * 100 + c
print(p1)
