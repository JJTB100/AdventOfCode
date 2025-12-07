with open("input.in") as f:
    lines = f.readlines()

grid = [[c for c in line.strip()] for line in lines]

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            grid[y][x] = 1
        elif grid[y][x] == ".":
            grid[y][x] = 0
print(grid)
p1 = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        # Check if last row
        if y != len(grid) - 1:
            if not(isinstance(c, str)) and c > 0:
                # Check the square below for "^" 
                if grid[y+1][x] == '^':
                    p1 += 1
                    # If it is, add "c" either side
                    grid[y+1][x-1] = grid[y+1][x-1] + c
                    grid[y+1][x+1] = grid[y+1][x+1] + c
                    # If not, put "c" in that square
                else:
                    grid[y+1][x] = grid[y+1][x] +c
print(p1)
print(sum(grid[len(grid)-1]))
"""
for row in grid:
    line = ""
    for c in row:
        line += str(c)
    print(line)"""