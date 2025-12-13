# Algorithm X
# Matrix of moves in the rows and constraints in the columns
# Primary Cols: Shapes
# Secondary Cols: Coords
# https://en.wikipedia.org/wiki/Knuth%27s_Algorithm_X
# Must Pre-calculate rotations and reflections
# Each row: "Shape X, Instance Y, placed at (r, c) with Rotation R."
# 

## Pre-Processing the Rotations and Flipping
# Take a shape and generate all 8 symmetries
# Deduplicate i.e. remove symmetries that are the same
# Generate Rows on the matrix by shifting the unique shapes to every valid (x,y) on the grid

## Algorithm X (Dancing Links)
# Pick a Primary Col <with the fewest 1s> (fewest valid moves for that piece)
# Select a row that covers this column
#   Remove the primary col (constraints met)
#   Remove all secondary cols (cells) occupied by that row
#   Remove all other rows that needed any of those grid cells
#   Remove all other rows that used the same piece

with open("input.in") as f:
    lines = f.readlines()

p1 = 0
for line in lines:
    if len(line) > 5:
        if (int(line[0:2]) * int(line[3:5])) >= (9 * sum(int(num) for num in line.split(": ")[1].split(" "))):
            p1 += 1
            
print(p1)