import re; print(sum(int(match[1]) * int(match[2]) for match in re.findall("(mul)\((\d+),(\d+)\)", open("input.txt", "r").read())))

