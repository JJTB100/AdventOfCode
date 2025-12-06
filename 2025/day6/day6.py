import math


with open("input.in") as f:
    data = f.readlines()

data = list((line.strip().split(" ") for line in data))
newData = []
arithmetic = []
for line in data:
    newLine = []
    for num in line:
        if num == "*" or num == "+":
            arithmetic.append(num)
        elif num != '':
            newLine.append(int(num))
    newData.append(newLine)
data = newData[:-1] 


p1 = 0
for col, a in enumerate(arithmetic):
    #print(a)
    if a == '*':
        p1 += math.prod(data[i][col] for i in range(len(data)))
    elif a == '+':
        p1 += sum(data[i][col] for i in range(len(data)))

print(p1)

with open("input.in") as f:
    data = [line.rstrip("\n") for line in f.readlines()]

p2=0
mode = data[len(data)-1][0]
currentCol = []
for col in range(len(data[0])):
    currentNum = ""
    for row in range(len(data)):
        c = data[row][col]
        if row == len(data)-1:
            # Arithmetic row
            if c != ' ' and col != 0:
                colMath = sum(currentCol) if mode == "+" else math.prod(currentCol)
                #print(f"{currentCol}, {mode=}, {col=}, {colMath=}")
                p2 += colMath
                mode = c  
                currentCol = []
        else:
            if c.isnumeric():
                #print(f"{currentNum=}")
                currentNum+=c
    if currentNum != '':
        currentCol.append(int(currentNum))

colMath = sum(currentCol) if mode == "+" else math.prod(currentCol)
p2 += colMath
print(p2)
