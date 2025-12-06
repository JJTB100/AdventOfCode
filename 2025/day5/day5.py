from itertools import combinations

with open("input.in") as f:
    data = f.read()

ranges = list(((n.strip().split("-")) for n in data.split("\n\n")[0].split("\n")))
#IDs = list(data.split("\n\n")[1].split("\n"))
"""
p1=0
for id in IDs:
    for low, high in ranges:
        if int(low) <= int(id) <= int(high):
            p1+=1
            #print(id)
            break
        
print(p1)
"""
p2 = 0
ranges.sort(key=lambda r: int(r[0]))
ranges = [[int(l), int(h)] for l,h in ranges]
newRanges = []
currentRange = ranges[0]

print(ranges)
for i in range(1, len(ranges)):
    print(f"{currentRange=}, {ranges[i]=}")
    if ranges[i][0] <= currentRange[1]: #if next range start is less than current range end
        # extend current range
        currentRange[1] = max(ranges[i][1], currentRange[1])
        print("EXTEND")
    else:
        newRanges.append(currentRange)
        currentRange = ranges[i]
        print("PUT")
newRanges.append(currentRange)

print(newRanges)
p2 = sum(int(high)-int(low)+1 for low, high in newRanges)
    
print(p2)