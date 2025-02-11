with open("input.in", "r") as f:
    lines = list(map(int, f.read().splitlines()))

import time
start = time.time()


def mix(n1, n2):
    return (n1 ^ n2) % 16777216


def next_num(n):
    n = mix(64*n, n)
    n = mix(n//32, n)
    n = mix(n * 2048, n)
    return n


ranges = {}

for num in lines:
    seed = num
    visited = set()
    changes = []

    for _ in range(2000):
        nextSeed = next_num(seed)
        changes.append((nextSeed % 10) - (seed % 10))
        seed = nextSeed

        if len(changes) == 4:
            key = ",".join(map(str, changes))
            if key not in visited:
                if key not in ranges:
                    ranges[key] = []
                ranges[key].append(nextSeed % 10)
                visited.add(key)
            changes.pop(0)

print(max(sum(rangeValues) for rangeValues in ranges.values()))
print(time.time() - start )
