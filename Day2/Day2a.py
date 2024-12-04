
def is_safe(levels):
    if len(levels) <= 1:
        return True

    direction = levels[1] - levels[0]
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        if diff * direction <= 0 or abs(diff) > 3:
            return False

    return True

def count_safe_reports(reports):
    count = 0
    for report in reports:
        levels = [int(level) for level in report.split()]
        if is_safe(levels):
            count += 1
    return count
        

f = open("input.txt")
reports = f.readlines()

print(count_safe_reports(reports))
