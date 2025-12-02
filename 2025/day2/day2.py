from functools import cache
with open("input.in") as f:
    line = f.read()

input = list(line.strip().split(","))

@cache
def getFactorPairs(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return sorted(factors)

p1=0
p2=0
for id_range in input:
    for id in range(int(id_range.split("-")[0]), int(id_range.split("-")[1])+1):
        if str(id)[:len(str(id))//2] == str(id)[len(str(id))//2:]:
            p1 += id
        str_id = str(id)
        length = len(str_id)
        for fac1, fac2 in getFactorPairs(length):
            if str_id == str_id[:fac1]*fac2 and fac2 >1 or str_id == str_id[:fac2]*fac1 and fac1 > 1:
                p2 += id
                #print(id)
                break



print(p1, p2)