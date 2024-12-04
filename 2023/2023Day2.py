lines = open("2023/input.txt", "r").readlines()

total = 0
for line in lines:

    sets = (line.split(": ", 1)[1].split("; "))
    gameDict = {}
    for set in sets:
        for el in set.split(", "):
            key = el.split(" ")[1].strip()
            value = int(el.split(" ")[0])
            if gameDict.get(key, 0) < value:
                gameDict[key] = value

    total += gameDict["red"] * gameDict["blue"] * gameDict["green"]

print(total)
