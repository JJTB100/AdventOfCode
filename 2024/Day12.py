import sys
from collections import deque


def calculate_area_and_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()
    total_area_perimeter = 0
    total_area_sides = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue

            area, perimeter, sides = explore_region(grid, r, c, seen)
            total_area_perimeter += area * perimeter
            total_area_sides += area * sides

    return total_area_perimeter, total_area_sides


def explore_region(grid, row, col, seen):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(row, col)])
    area = 0
    perimeter = 0
    perimeter_cells = {}  # Store perimeter cells by direction

    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue

        seen.add((r, c))
        area += 1

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:  # up, right, down, left
            rr, cc = r + dr, c + dc
            if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == grid[r][c]:
                queue.append((rr, cc))
            else:
                perimeter += 1
                perimeter_cells.setdefault((dr, dc), set()).add((r, c))

    sides = count_sides(perimeter_cells)
    return area, perimeter, sides


def count_sides(perimeter_cells):
    sides = 0
    for direction, cells in perimeter_cells.items():
        seen_perimeter = set()
        for pr, pc in cells:
            if (pr, pc) not in seen_perimeter:
                sides += 1
                explore_side(cells, pr, pc, seen_perimeter)
    return sides


def explore_side(cells, row, col, seen_perimeter):
    queue = deque([(row, col)])
    while queue:
        r, c = queue.popleft()
        if (r, c) in seen_perimeter:
            continue
        seen_perimeter.add((r, c))
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr, cc = r + dr, c + dc
            if (rr, cc) in cells:
                queue.append((rr, cc))


infile = 'input.in'
with open(infile) as f:
    grid = f.read().strip().split('\n')
p1, p2 = calculate_area_and_perimeter(grid)
print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
