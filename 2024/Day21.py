with open("example.in", "r") as f:
    lines = f.read().splitlines()

dir_mapper = {"A": 0, "^": 1, ">": 2, "<": 3, "v": 4}
num_mapper = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
              "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10}
directional_map = [["", "<", "v", "<v>", "<v"],
                   [">", "", "v>", "v<", "v"],
                   ["^", "<^", "", "<<", "<"],
                   [">>^", ">^", ">>", "", ">"],
                   [">^", "^", ">", "<", ""]]
numerical_map = [["", "^<", "^", "^>", "^^<", "^^", "^^>", "^^^<", "^^^", "^^^>", ">"],
                 [">v", "", ">", ">>", "^", "^>",
                     "^>>", "^^", "^^>", "^^>>", ">>v"],
                 ["v", "<", "", ">", "<^", "^", "^>", "^^<", "^^", "^^>", ">v"],
                 ["<v", "<<", "<", "", "^<<", "^<", "^", "^^<<", "^^<", "^^", "v"],
                 [">vv", "v", "v>", "v>>", "", ">",
                     ">>", "^", "^>", "^>>", ">>vv"],
                 ["vv", "v<", "v", "v>", "<", "", ">", "<^", "^", "^>", ">vv"],
                 ["vv<", "v<<", "v<", "v", "<<", "<", "", "^<<", "^<", "^", "vv"],
                 [">vvv", "vv", "vv>", "vv>>", "v", "v>", "v>>", "", ">", ">>"],
                 ["vvv", "vv<", "vv", "vv>", "v<", "v", "v>", "<", "", ">", "vvv>"],
                 ["vvv<", "vv<<", "vv<", "vv", "v<<",
                     "v<", "v", "<<", "<", "", "vvv"],
                 ["<", "^<<", "^<", "^", "^^<<", "^<", "^^", "^^^<<", "^^^<", "^^^", ""]]


def get_direction_instr(start, end):
    return directional_map[dir_mapper[start]][dir_mapper[end]] + "A"


def get_numerical_instr(start, end):
    return numerical_map[num_mapper[start]][num_mapper[end]] + "A"


for line in lines:
    line = "A"+line
    output = ""
    for i in range(1, len(line)):
        output += get_numerical_instr(line[i-1], line[i])
    print(output)
    for i in range(1, len(output)):
        output = output[:i] + \
            get_direction_instr(output[i-1], output[i]) + output[i:]

    print(output)
