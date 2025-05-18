""" Advent Of Code 2019 : 1 """

from aoctools import *

def get_fuel(number, total):
    if number <= 0:
        return total - number
    new = number // 3 - 2
    return get_fuel(new, total + new)

def main(aocd: AOCD):
    numbers = aocd.ilist
    aocd.p1(sum((num // 3 - 2) for num in numbers))
    aocd.p2(sum(get_fuel(num, 0) for num in numbers))


if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2019, 1)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
