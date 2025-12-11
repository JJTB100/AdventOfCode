from collections import deque
import re
import numpy as np
import scipy

with open("input.in") as file:
    lines = file.read()

class Machine:
    def __init__(self, l, b, r):
        self.lights = l
        self.buttons = b
        self.reqs = r
        self.pressed = []
    def __str__(self):
        return f"Lights {self.lights} :: Buttons {self.buttons} :: Reqs {self.reqs} :: pressed {self.pressed}"
    
machines = []
pattern = re.compile(r"\[([.#]+)\]((?:\s+\(\d+(?:,\d+)*\))+)\s+\{([\d,]+)\}")
for match in re.findall(pattern, lines):
    lights, buttons, reqs = [],[],[]
    for c in match[0]:
        lights.append(True) if c=='#' else lights.append(False)
    for button in match[1].strip().split(" "):
        button = list(int(n) for n in button.lstrip("(").rstrip(")").split(","))
        buttons.append(button)
    for req in match[2].split(","):
        reqs.append(int(req))
    machines.append(Machine(lights, buttons, reqs))

p1 = 0
for n,m in enumerate(machines):
    button_masks = []
    for b_indices in m.buttons:
        mask = 0
        for idx in b_indices:
            mask |= (1 << idx)
        button_masks.append(mask)

    current_state = 0
    for i, is_on in enumerate(m.lights):
        if is_on:
            current_state |= (1 << i)

    # BFS
    queue = deque([(current_state, [])]) 
    visited = {current_state}            

    solved = False
    while queue:
        state, path = queue.popleft()
        
        if state == 0: # All lights off
            p1 += len(path)
            #print(f"Solved with path: {path}")
            solved = True
            break
        
        for i, mask in enumerate(button_masks):
            new_state = state ^ mask
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [i])) 

    if not solved:
        print("No solution found")
    
print(f"{p1=}")

p2=0
for m in machines:
    # Buttons * How many times per button = Requirements
    A = np.zeros((len(m.reqs), len(m.buttons)), dtype=int)
    for col_i, button in enumerate(m.buttons):
        for row_i in button:
            A[row_i,col_i]=1
    b = np.array(m.reqs)
    constraints = scipy.optimize.LinearConstraint(A, b, b)
    res = scipy.optimize.milp(c=np.ones(len(m.buttons)), constraints=constraints, integrality=np.ones(len(m.buttons)))
    if res.success:
        p2+=int(sum(np.round(res.x)))
print(f"{p2=}")