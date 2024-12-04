import math as m
import re

# input lines
board = list(open("2023/input.txt"))
# get coords of all chars -> dict[(int, int): []]
chars = {(i, j): [] for i in range(140) for j in range(140)
         if board[i][j] not in "1234567890."}

# iterate over the rows
for r, row in enumerate(board):
    # find all numbers in the row
    for n in re.finditer(r"\d+", row):
        # get coords surrounding nums -> list[(int, int)]
        """
        -----------j-1-----------------
        start-1 (start match end) end+1
        -----------j+1-----------------
        """
        edge = {(j+r, i) for i in range(n.start()-1, n.end()+1) for j in range(-1, 2)
                # make sure we're not on the edge
                if 0 < i < len(board)-1 and 0 < r+j < len(board[0])-1}

        # for each intersection of chars and edge
        for coord in edge & chars.keys():
            chars[coord].append(int(n.group()))
            print(coord, chars[coord])

print(f"Part 1: {sum((sum(p) for p in chars.values()))}")
print(f"Part 2: {sum(m.prod(p) for p in chars.values() if len(p) == 2)}")
