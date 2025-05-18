""" Advent Of Code 2019 : 2 """

from aoctools import *


def main(aocd: AOCD):
    for n in range(100):
        for j in range(100):
            intcode = aocd.ilist_split_at(",")
            intcode[1] = n
            intcode[2] = j
            try:
                i = 0
                while True:
                    if intcode[i] == 1:
                        intcode[intcode[i+3]] = intcode[intcode[i+1]] + intcode[intcode[i+2]]
                    elif intcode[i] == 2:
                        intcode[intcode[i+3]] = intcode[intcode[i+1]] * intcode[intcode[i+2]]
                    elif intcode[i] == 99:
                        break
                    i += 4
                if intcode[0] == 19690720:    
                    aocd.p2(n * 100 + j)
            except:
                pass


if __name__ == '__main__':
    import time
    start = time.time()
    aocd = AOCD(2019, 2)
    main(aocd)
    print(f'Time Taken: {time.time() - start} seconds')
