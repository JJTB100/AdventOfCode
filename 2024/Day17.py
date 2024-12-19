import sys
with open("input.in", "r") as f:
    lines = f.read().split("\n")

A = int(lines[0][12:])
B = int(lines[1][12:])
C = int(lines[2][12:])

sys.setrecursionlimit(10**6)

instructions = lines[4][9:].split(",")
instructions = list(map(int, instructions))
program_out = ""

ins = 0
while ins < len(instructions):
    literal_operand = instructions[ins+1]
    match literal_operand:
        case 0 | 1 | 2 | 3:
            combo_operand = literal_operand
        case 4:
            combo_operand = A
        case 5:
            combo_operand = B
        case 6:
            combo_operand = C
        case 7:
            pass
    match instructions[ins]:
        case 0:
            # adv -> Right Shift A by . into A
            A = int(A/(2**combo_operand))
            ins += 2
        case 1:
            # bxl -> XOR
            B = B ^ literal_operand
            ins += 2
        case 2:
            # bst ->
            B = combo_operand % 8
            ins += 2
        case 3:
            # jnz
            if A != 0:
                ins = literal_operand
            else:
                ins += 2
        case 4:
            # bxc
            B = B ^ C
            ins += 2
        case 5:
            # out
            program_out += str(combo_operand % 8) + ","
            ins += 2
        case 6:
            # bdv -> Right Shift A by . into B
            B = int(A/(2**combo_operand))
            ins += 2
        case 7:
            # cdv -> Right Shift A by . into C
            C = int(A/(2**combo_operand))
            ins += 2

program_out = program_out[:-1]


def step(A):
    """Run a single loop."""
    B = A % 8
    B = B ^ 5
    C = A // (2**B)
    B = B ^ C
    B = B ^ 6
    # Only return the last 3 bits
    return B % 8


def find(A, pos=0):
    """Searches for a value of A that works"""
    # If the value returned by running the program once is not the end of the list, it's not the right A
    if step(A) != instructions[-(pos + 1)]:
        return
    # BASE case: stop if we've got the whole list, we've found a good value for A
    if pos == len(instructions) - 1:
        As.append(A)
    else:
        for B in range(8):
            # look at the next number, try each possible 1-8
            find(A * 8 + B, pos + 1)


As = []
for a in range(8):
    # Try every possible value of A for the end of the list
    find(a)
print(As[0])
