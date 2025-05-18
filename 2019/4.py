""" Advent Of Code 2019 : 4 """

from collections import Counter
from aoctools import *

def isValid(password):
    for i in range(1, 6):
        if password[i] < password[i-1]:
            return False
    if 2 in Counter(password).values():
        return True 
    return False
        
def main(aocd: AOCD):
    print(isValid('123444'))
    p1 = 0
    for i in range(245182, 790572):
        p1 += 1 if isValid(str(i)) else 0
    print(p1)


if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2019, 4)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
