def is_safe(levels):
    if len(levels) <= 1:
        return True

    direction = levels[1] - levels[0]
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff * direction <= 0 or abs(diff) > 3:
            return False

    return True

def is_safe_with_dampener(levels):
    for i in range(len(levels)):
        new_levels = levels[:i] + levels[i+1:]
        if is_safe(new_levels):
            return True
    return False

def count_safe_reports(reports):
    count = 0
    for report in reports:
        levels = [int(level) for level in report.split()]
        if is_safe_with_dampener(levels):
            count += 1
    return count

# Read input from a file
with open("input.txt", "r") as f:
    reports = f.readlines()



print(count_safe_reports(reports))
