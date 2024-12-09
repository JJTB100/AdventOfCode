from itertools import combinations
with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def run(p1=False):
    # get all antennas {name:[(), ()], name:[(), ()], ..}
    antennas = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c != ".":
                if antennas.get(c, -1) == -1:
                    antennas[c] = []
                antennas[c].append((y, x))

    antinodes = set()  # {(), (), ..}
    # compare combinations of antennas with the same type
    for key in antennas:
        for c1, c2 in combinations(antennas[key], 2):
            diffY = c2[0] - c1[0]
            diffX = c2[1] - c1[1]
            y = c2[0] if not p1 else c2[0] + diffY
            x = c2[1] if not p1 else c2[1] + diffX
            # after
            while 0 <= y < len(lines) and 0 <= x < len(lines[0]):
                antinodes.add((y, x))
                y = y + diffY
                x = x + diffX
                if p1:
                    break

            y = c1[0] if not p1 else c1[0] - diffY
            x = c1[1] if not p1 else c1[1] - diffX
            # before
            while 0 <= y < len(lines) and 0 <= x < len(lines[0]):
                antinodes.add((y, x))
                y = y - diffY
                x = x - diffX
                if p1:
                    break

    return len(antinodes)


print(run(True), run())
