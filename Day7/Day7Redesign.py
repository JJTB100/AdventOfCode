import re
from operator import add, mul


def run(equations, ops):
    result = 0
    for target, first, *rest in equations:
        queue = [first]
        for value in rest:
            # Remakes the queue but with values equal to the effects of each operator
            # on the next number in the equation. doesn't add it to the queue if we've gone over the target
            queue = [op(total, value) for total in queue for op in ops
                if total <= target]
        if target in queue:
            result += target
    return result


with open("input.txt", "r") as f:
    input = f.read().splitlines()

lines = []
for line in input:
    lines.append(list(map(int, re.findall(r"\d+", line))))


def concat(e1, e2):
    return int(str(e1) + str(e2))


print(run(lines, (add, mul)))
print(run(lines, (add, mul, concat)))
