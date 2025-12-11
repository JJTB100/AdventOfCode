from itertools import combinations

with open("input.in") as f:
    data = [line.strip() for line in f.readlines()]

coords = []
for line in data:
    x, y = line.split(",")
    coords.append((int(x), int(y)))

def is_on_boundary(p, polygon):
    x, y = p
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        # Check if point is on this segment (Horizontal or Vertical)
        if p1[0] == p2[0] == x: # Vertical Edge
             if min(p1[1], p2[1]) <= y <= max(p1[1], p2[1]): return True
        elif p1[1] == p2[1] == y: # Horizontal Edge
             if min(p1[0], p2[0]) <= x <= max(p1[0], p2[0]): return True
    return False
    
def ray_cast_is_inside(point, polygon):
    x, y = point
    num_vertices = len(polygon)
    crossings = 0

    for i in range(num_vertices):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % num_vertices]
        if (y1 > y) != (y2 > y) and x <= ((x2 - x1) * (y - y1) / (y2 - y1) + x1):
            crossings += 1
    return crossings % 2 == 1

p1 = 0
p2 = 0
for c1, c2 in sorted(combinations(coords,2), key=lambda c: (abs(c[0][0]-c[1][0])+1)*(abs(c[0][1]-c[1][1])+1), reverse=True):
    size = (abs(c1[0]-c2[0])+1)*(abs(c1[1]-c2[1])+1)
    c3, c4 = (c1[0], c2[1]), (c2[0], c1[1])
    c3_valid = is_on_boundary(c3, coords) or ray_cast_is_inside(c3, coords)
    c4_valid = is_on_boundary(c4, coords) or ray_cast_is_inside(c4, coords)
    # Check if all 4 corners are inside
    if size > p1:
        p1 = size 
    if c3_valid and c4_valid:        ## Edge Check
        # Define bounds
        min_x = min(c1[0], c2[0])
        max_x = max(c1[0], c2[0])
        min_y = min(c1[1], c2[1])
        max_y = max(c1[1], c2[1])
        # for each edge in polygon
        valid = True
        for i in range(len(coords)):
            e1 = coords[i]
            e2 = coords[(i+1)%len(coords)]
            # if vertical edge (const x)
            if e1[0] == e2[0]:
                ey_min, ey_max = sorted((e1[1], e2[1]))
                # is the edge's x between min_x and max_x and does the edge's y-range overlap with the rectangle's Y-range
                if min_x < e1[0] < max_x and (ey_min < max_y and ey_max > min_y):
                    valid = False
                    break
            # if horizontal edge (const y)
            if e1[1] == e2[1]:
                ex_min, ex_max = sorted((e1[0], e2[0]))
                # is the edge's y between min_y and max_y and does the edge's X-range overlap with the rectangle's X-range
                if min_y < e1[1] < max_y and (ex_min < max_x and ex_max > min_x):
                    valid = False
                    break
        # Valid rect if here
        if size > p2 and valid:
            p2 = size
            break
    
print(f"{p1=},{p2=}")