lines = list(open("input.txt", "r"))

# find all Xs
xes = list((r, c) for r in range(140) for c in range(140)
           if lines[r][c] == "X")

total = 0
for x in xes:
    # find all edge squares
    edgeSqrs = [(x[0]+i, x[1]+j) for i in range(-1, 2) for j in range(-1, 2)
                if -1 < x[0]+i < 140 and -1 < x[1]+j < len(lines[0])]
    for edge in edgeSqrs:
        if lines[edge[0]][edge[1]] == "M":
            # find the direction
            diffi = x[0] - edge[0]
            diffj = x[1] - edge[1]
            # subtract the direction and check if it's correct
            if 0 <= edge[0]-diffi < len(lines) and 0 <= edge[1]-diffj < len(lines[0]) and lines[edge[0] - diffi][edge[1] - diffj] == "A":
                if 0 <= edge[0]-2*diffi < len(lines) and 0 <= edge[1]-2*diffj < len(lines[0]) and lines[edge[0] - 2*diffi][edge[1] - 2*diffj] == "S":
                    total += 1

print(total)
