
with open("Day1/input.txt") as f:
    input = f.readlines()

firstList = [int(line[:5]) for line in input]
secondList = [int(line[-6:-1]) for line in input]

# A dictionary storing how many times a number occurs
# Could use collections.Counter: second_counts = Counter(secondList)
secondCounts = {}
for number in secondList:
    secondCounts[number] = secondCounts.get(number, 0) + 1

total = 0
for firstNum in firstList:
    total += firstNum * secondCounts.get(firstNum, 0)

print(total)
