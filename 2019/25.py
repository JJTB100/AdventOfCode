""" Advent Of Code 2019 : 25 """

from aoctools import *


def main(aocd: AOCD):
    aocd.get_example()


if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2019, 25)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
