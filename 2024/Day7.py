
import re


def RecMulAdd(l, target):
    totals = []
    totals = Mul(l[1:], [], l[0], target)
    totals += Add(l[1:], [], l[0], target)
    totals += Concat(l[1:], [], l[0], target)
    return totals


def Mul(l, totals, subTotal, target):
    if len(l) == 0:
        if subTotal <= target:
            totals.append(subTotal)
        return totals
    else:
        subTotal = subTotal * l[0]
        if subTotal <= target:
            Mul(l[1:], totals, subTotal, target)
            Add(l[1:], totals, subTotal, target)
            Concat(l[1:], totals, subTotal, target)
    return totals


def Add(l, totals, subTotal, target):
    if len(l) == 0:
        if subTotal <= target:
            totals.append(subTotal)
        return totals
    else:
        subTotal = subTotal + l[0]
        if subTotal <= target:
            Mul(l[1:], totals, subTotal, target)
            Add(l[1:], totals, subTotal, target)
            Concat(l[1:], totals, subTotal, target)
    return totals


def Concat(l, totals, subTotal, target):
    if len(l) == 0:
        if subTotal <= target:
            totals.append(subTotal)
        return totals
    else:
        subTotal = int(str(subTotal) + str(l[0]))
        if subTotal <= target:
            Mul(l[1:], totals, subTotal, target)
            Add(l[1:], totals, subTotal, target)
            Concat(l[1:], totals, subTotal, target)
    return totals


with open("input.txt", "r") as f:
    input = f.read().splitlines()

lines = []
for line in input:
    lines.append(list(map(int, re.findall(r"\d+", line))))

print(lines)
sum = 0
for l, line in enumerate(lines):
    print(l)
    if line[0] in RecMulAdd(line[1:], line[0]):
        sum += line[0]

print(sum)
