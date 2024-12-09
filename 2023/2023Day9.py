with (open("input.txt", "r") as f):
    lines = f.read().splitlines()
lines = list(list(map(int, line.split(" "))) for line in lines)


def recursiveNext(numbers):
    differences = list(numbers[i]-numbers[i-1] for i in range(1, len(numbers)))
    # Base case:
    if all(number == 0 for number in differences):
        return numbers[0]
    # Recursive case:
    else:
        return numbers[-1] + recursiveNext(differences)


def recursiveBefore(numbers):
    differences = list(numbers[i]-numbers[i-1] for i in range(1, len(numbers)))
    print(differences)
    # Base case:
    if all(number == 0 for number in differences):
        return numbers[0]
    # Recursive case:
    else:
        return numbers[0] - recursiveBefore(differences)


total = 0
for line in lines:
    print(recursiveBefore(line))
    total += recursiveBefore(line)
print(total)
