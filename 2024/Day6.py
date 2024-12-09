import numpy as np

with open("input.txt") as f:
    input = f.read().splitlines()
lines = []
for line in input:
    new = []
    new[:] = line
    lines.append(new)

# Find The Guard (track pos)
pos = []
for l, line in enumerate(lines):
    if "^" in line:
        x, y = line.index("^"), l
        pos.append((x, y))


x, y = pos[0]
forward = 1
# Loop
while 0 <= x < len(lines[0]) and 0 <= y < len(lines):  # of next!
    # check if forward is a #
    if lines[y][x] == "#":
        # change forward direction
        forward = forward + 1 if forward != 4 else 1
        # print("Forward: ", forward)
        pos.pop()
        x, y = pos[len(pos)-1]

    # move forward
    if forward == 1:
        y = y-1
    elif forward == 2:
        x = x + 1
    elif forward == 3:
        y = y + 1
    elif forward == 4:
        x = x - 1

    # print(x, y)
    pos.append((x, y)) if (x, y) not in pos else 0


# out
pos.pop()
print(pos)
print(len(pos))
