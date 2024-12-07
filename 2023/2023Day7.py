from collections import Counter
from functools import cmp_to_key


def customCardCompare(card1, card2):
    cardNums = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                "8": 8, "9": 9, "T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    card1 = cardNums[card1]
    card2 = cardNums[card2]
    if card1 == card2:
        return 0
    elif card1 > card2:
        return 1
    elif card2 > card1:
        return -1


def customCompare(hand1, hand2):
    c1, c2 = [], []
    c1[:] = hand1[0]
    c2[:] = hand2[0]
    c1Jokers = c1.count("J")
    c2Jokers = c2.count("J")


    c1NJ = c1.copy()
    c2NJ = c2.copy()
    
    while "J" in c1NJ:
        c1NJ.remove("J")
    while "J" in c2NJ:
        c2NJ.remove("J")

    counter1 = list(Counter(c1NJ).values())
    counter2 = list(Counter(c2NJ).values())
    counter1.sort(reverse=True)
    counter2.sort(reverse=True)
    if len(counter1) == 0:
        counter1.append(5)
    else:
        counter1[0] += c1Jokers

    if len(counter2) == 0:
        counter2.append(5)
    else:
        counter2[0] += c2Jokers
        
    print(f"Comparing {counter1}, {counter2}, {c1}, {c2}")

    if counter1 == [5] and counter2 == [5]:
        for i in range(len(c1)):
            card1 = c1[i]
            card2 = c2[i]
            if customCardCompare(card1, card2) != 0:
                return customCardCompare(card1, card2)
    elif counter1 == [5]:
        return 1
    elif counter2 == [5]:
        return -1
# 4 of a kind
    if counter1 == [4, 1] and counter2 == [4, 1]:
        for i in range(len(c1)):
            card1 = c1[i]
            card2 = c2[i]
            if customCardCompare(card1, card2) != 0:
                return customCardCompare(card1, card2)
    elif counter1 == [4, 1]:
        return 1
    elif counter2 == [4, 1]:
        return -1

    # Full House
    elif counter1 == [3, 2] and counter2 == [3, 2]:
        for i in range(len(c1)):
            card1 = c1[i]
            card2 = c2[i]
            if customCardCompare(card1, card2) != 0:
                return customCardCompare(card1, card2)
    elif counter1 == [3, 2]:
        return 1
    elif counter2 == [3, 2]:
        return -1

    # 3 of a kind
    elif counter1 == [3, 1, 1] and counter2 == [3, 1, 1]:
        for i in range(len(c1)):
            card1 = c1[i]
            card2 = c2[i]
            if customCardCompare(card1, card2) != 0:
                return customCardCompare(card1, card2)
    elif counter1 == [3, 1, 1]:
        return 1
    elif counter2 == [3, 1, 1]:
        return -1

    # Two pair
    elif counter1 == [2, 2, 1] and counter2 == [2, 2, 1]:
        for i in range(len(c1)):
            card1 = c1[i]
            card2 = c2[i]
            if customCardCompare(card1, card2) != 0:
                return customCardCompare(card1, card2)
    elif counter1 == [2, 2, 1]:
        return 1
    elif counter2 == [2, 2, 1]:
        return -1

    # One pair
    elif counter1 == [2, 1, 1, 1] and counter2 == [2, 1, 1, 1]:
        for i in range(len(c1)):
            card1 = c1[i]
            card2 = c2[i]
            if customCardCompare(card1, card2) != 0:
                return customCardCompare(card1, card2)
    elif counter1 == [2, 1, 1, 1]:
        return 1
    elif counter2 == [2, 1, 1, 1]:
        return -1

    # High
    elif counter1 == [1, 1, 1, 1, 1] and counter2 == [1, 1, 1, 1, 1]:
        for i in range(len(c1)):
            card1 = c1[i]
            card2 = c2[i]
            if customCardCompare(card1, card2) != 0:
                return customCardCompare(card1, card2)


# ----------------------------------------------
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

hands = []
for line in lines:

    hands.append(tuple(line.split(" ")))

hands = sorted(hands, key=cmp_to_key(customCompare))

total = 0
for i, hand in enumerate(hands):
    print(hand)
    total += int(hand[1]) * (i + 1)

print(total)
