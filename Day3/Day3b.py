import re
reg = re.findall("(mul)\((\d+),(\d+)\)|(do\(\))|(don't\(\))",
                 open("input.txt", "r").read())

total, going = 0, True

for match in reg:
    going = True if match[3] == "do()" else False if match[4] == "don't()" else going
    total += int(match[1]) * int(match[2]) if going else 0

print(total)
