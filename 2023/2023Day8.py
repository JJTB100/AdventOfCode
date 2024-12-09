import math
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
lines = [line.split(" = ") for line in lines]
instructs = lines[0][0]
lines = lines[2:]
for line in lines:
    line[1] = list(line[1].split(", "))
    line[1][0] = line[1][0][1:]
    line[1][1] = line[1][1][:-1]
print(instructs)
guide = {lines[i][0]: (lines[i][1][0], lines[i][1][1])
         for i in range(len(lines))}
print(guide)


def doStep(start, char):
    current = guide[start]
    if char == "L":
        return (current[0])
    elif char == "R":
        return (current[1])


starting_locations = []
for location in guide:
    if location[-1] == "A":
        starting_locations.append(location)
queue = starting_locations.copy()


AllSteps = []
for location in queue:
    i = 0
    steps = 0
    while location[-1] != "Z":
        steps += 1
        location = doStep(location, instructs[i])
        if i == len(instructs)-1:
            i = 0
        else:
            i += 1
    AllSteps.append(steps)

print(math.lcm(*AllSteps))
