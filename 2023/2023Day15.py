with open("input.in", "r") as file:
    data = file.read().strip()
    data = data.split(",")


def HASH(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value = current_value * 17
        current_value = current_value % 256
    return current_value


def contains(list, string):
    for i, s in enumerate(list):
        if string in s:
            return i
    return -1


boxes = {}
for i in range(256):
    boxes[i] = []
for s in data:
    
    if "=" in s:
        hash = HASH(s[:-2])
        if contains(boxes[hash], s[:-2]) != -1:
            boxes[hash][contains(boxes[hash], s[:-2])] = s
        else:
            boxes[hash].append(s)
    elif "-" in s:
        s += "-"
        hash = HASH(s[:-2])
        if contains(boxes[hash], s[:-2]) != -1:
            boxes[hash].pop(contains(boxes[hash], s[:-2]))

p2 = 0
for box in boxes:
    for i, lens in enumerate(boxes[box]):
        p2 += int(1+box) * int(1+i) * int(lens[-1])
print(p2)
