with open("input.txt") as f:
    lines = f.readlines()
input = list((line[:5], line[-6:]) for line in lines)

first, second = [sorted(map(int, list(lst))) for lst in zip(*input)]

total = 0
for i in range(len(first)):
    total += abs(first[i]-second[i])

print(total)
