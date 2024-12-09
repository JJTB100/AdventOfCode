lines = list(open("input.txt", "r"))

aes = list((r, c) for r in range(1, 139) for c in range(1, 139)
           if lines[r][c] == "A")

total = 0
for a in aes:
    if ({lines[a[0]-1][a[1]-1], lines[a[0]+1][a[1]+1]} == {"M", "S"}) and ({lines[a[0]+1][a[1]-1], lines[a[0]-1][a[1]+1]} == {"M", "S"}):
        total += 1
print(total)
