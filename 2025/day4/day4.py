grid = []
with open("input.in") as f:
    for line in f:
        grid.append([c for c in line.strip()])

def getFilledAdj(y, x):
    num =0
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0: 
                pass
            elif 0 <= x+i < len(grid[0]) and 0 <= y+j < len(grid):
                if grid[y+j][x+i] == '@':
                    num += 1
                    

    return num

p1 = 0
p2 = 0
movedPaper = 1
iterations = 0
newGrid = grid.copy()
while movedPaper != 0:
    movedPaper = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '@' and getFilledAdj(y,x) < 4:
                p1+=1
                movedPaper += 1
                if(iterations > 0):
                    newGrid[y][x] = 'x'
            print(grid[y][x], end="")
        print()
    print("^^^^" +str(iterations))
    p2 += movedPaper
    iterations += 1
    if(iterations == 1):
        print(p1)
    grid = newGrid.copy()
    
print(p2)