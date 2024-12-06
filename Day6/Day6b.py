def patrol(guard, obstacles, new_obstacle=None):
    if new_obstacle:
        obstacles.add(new_obstacle)
    pos, posdir = set(), set()

    while guard[0] in range(height) and guard[1] in range(width):
        y, x, forward = guard
        if (y, x, forward) in posdir:
            return None
        pos.add((y, x))
        posdir.add((y, x, forward))
        if forward == 1:
            if (y - 1, x) in obstacles:
                guard[2] = forward+1
                continue
            y -= 1
        elif forward == 2:
            if (y, x + 1) in obstacles:
                guard[2] = forward + 1
                continue
            x += 1
        elif forward == 3:
            if (y + 1, x) in obstacles:
                guard[2] = forward + 1
                continue
            y += 1
        elif forward == 4:
            if (y, x - 1) in obstacles:
                guard[2] = 1
                continue
            x -= 1
        guard[0] = y
        guard[1] = x
    return pos


with open("input.txt") as file:
    obstacles = set()
    height = 0
    for y, line in enumerate(file):
        for x, ch in enumerate(line.strip()):
            if ch in ("^"):
                guard = [y, x, 1]
                width = len(line) - 1
            elif ch == "#":
                obstacles.add((y, x))
        height += 1

pos = patrol(guard.copy(), obstacles.copy())

possible_new_obstacles = 0
for y, x in pos:
    if (y, x) in obstacles or y == guard[0] and x == guard[1]:
        continue
    if patrol(guard.copy(), obstacles.copy(), (y, x)) is None:
        possible_new_obstacles += 1

print(len(pos))
print(possible_new_obstacles)
