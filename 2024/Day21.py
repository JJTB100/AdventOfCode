from collections import Counter

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
UP, RIGHT, DOWN, LEFT = DIRECTIONS 

# Add two coordinate tuples
def add(*ps): return tuple(map(sum, zip(*ps)))

# Subtract two coordinate tuples
def sub(p1, p2):
    return tuple(a-b for a, b in zip(p1, p2))

with open("input.in") as file:
    lines = file.read().splitlines()

# Define both pads
num_pad_lines = """
789
456
123
.0A
""".strip().splitlines()

dir_pad_lines = """
.^A
<v>
""".strip().splitlines()

# Create dictionaries to map coordinates to characters and vice-versa for both pads
num_pad = {(i, j): c for i, line in enumerate(num_pad_lines)
           for j, c in enumerate(line) if c != "."}
dir_pad = {(i, j): c for i, line in enumerate(dir_pad_lines)
           for j, c in enumerate(line) if c != "."}

# Add reverse mappings (character to coordinates) for both pads
num_pad.update({v: k for k, v in num_pad.items()})
dir_pad.update({v: k for k, v in dir_pad.items()})

# Calculate a single step from source to target on a given pad
def step(source, target, pad):
    # Get Coords of source and target
    target_i, target_j = pad[target]
    source_i, source_j = pad[source]
    # Calc diffs
    di = target_i - source_i  
    dj = target_j - source_j

    # Construct movement string
    vert = "v"*di+"^"*-di
    horiz = ">"*dj+"<"*-dj

    # Prioritise straight then orthogonal moves
    if dj > 0 and (target_i, source_j) in pad:
        return vert+horiz+"A"
    # Check we don't hit the empty sqr
    if (source_i, target_j) in pad:
        return horiz+vert+"A"
    if (target_i, source_j) in pad:
        return vert+horiz+"A"

# Generate the full route for a path
def routes(path, pad):
    out = []
    start = "A"
    for next in path:
        # Get the route between each part of path
        out.append(step(start, next, pad))
        start = next 
    return "".join(out)

# transform input to moves on numpad
num_routes = []
for line in lines:  
    num_routes.append(routes(line, num_pad))
    
# transform numpad routes to dir routes
dir_routes = [routes(route, dir_pad) for route in num_routes]

# do the same again
dir_routes2 = [routes(route, dir_pad) for route in dir_routes]

p1 = 0
for route, line in zip(dir_routes2, lines):
    p1 += len(route) * int(line[:-1])
print("Part 1:", p1)


# same generate routes but use Counter for efficiency
def routes2(path, pad):
    out = []
    start = "A"
    for end in path:
        out.append(step(start, end, pad))
        start = end
    # Return a Counter of the routes
    return Counter(out)  


# Calculate the weighted length of routes stored in a Counter
def route_len(route):
    return sum(len(k)*v for k, v in route.items())

# Initialize routes as counters
robot_routes = [Counter([route]) for route in num_routes]
for _ in range(25):
    new_routes = []
    for route_counter in robot_routes:
        new_route = Counter()
        for sub_route, qty in route_counter.items():
            new_counts = routes2(sub_route, dir_pad)  # get route steps
            for k in new_counts:
                # Multiply counts by the quantity of the sub-route
                new_counts[k] *= qty
            new_route.update(new_counts)  # Update the new route counts
        new_routes.append(new_route)
    robot_routes = new_routes

p2 = sum(route_len(route)*int(line[:-1])
         for route, line in zip(robot_routes, lines))  # Calculate weighted sum of route lengths
print("Part 2:", p2)
