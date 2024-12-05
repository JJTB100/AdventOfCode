lines = open("input.txt").readlines()
total = 0
cards = {}
toDo = []


def scratchCard(card):
    global total
    total += 1
    if cards[card] == 0:
        return 0
    else:
        return sum(scratchCard(card + i) for i in range(1, cards[card]+1))


for line in lines:
    nums = line.strip().split(":")[1]
    winning = set(nums.split(" | ")[0].split())
    mine = set(nums.split(" | ")[1].split())
    cardNum = int(line.strip().split(":")[0][4:])
    cards[cardNum] = (len(winning & mine))

for cN in range(1, len(cards)+1):
    scratchCard(cN)


print(total)
