
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
guide = {lines[i][0]: (lines[i][1][0], lines[i][1][1]) for i in range(len(lines))}
print(guide)
def run():
    steps = 0
    current = guide["AAA"]
    while current != guide["ZZZ"]:
        for char in instructs:
            steps += 1
            if char == "L":
                current = guide[current[0]]
            elif char == "R":
                current = guide[current[1]]
            if current == guide["ZZZ"]:
                return steps
            
print(run())