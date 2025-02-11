from itertools import product
with open("input.in", "r") as f:
    chunks = f.read().strip().split("\n\n")

locks = []
keys = []
for chunk in chunks:
    chunk = chunk.split("\n")
    columns = {}  # [0-4]:int
    for i in range(len(chunk[0])):
        if i not in columns:
            columns[i] = -1
        for j in range(len(chunk)):
            if chunk[j][i] == "#":
                columns[i] += 1
    if chunk[0].startswith("#####"):
        # Lock
        locks.append(list(columns.values()))
    else:
        # Key
        keys.append(list(columns.values()))

p1 = 0
for key, lock in product(keys, locks):
    overlap = False
    for i in range(5):
        if key[i] + lock[i] > 5:
            overlap = True
            break
    if not overlap:
        print(key)

        p1 += 1

print(p1)
