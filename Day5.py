from functools import cmp_to_key

def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    rules = []
    updates = []
    lookups = [] # list of dicts

    for line in input:
        if line == '':
            continue
        if '|' in line:
            rule = line.split('|')
            rules.append(tuple(rule))
        else:
            update = line.split(',')
            if len(update) > 0:
                updates.append(tuple(update))

    for update in updates:
        lookup = {}
        for p, page in enumerate(update):
            lookup[page] = p
        lookups.append(lookup)

    return rules, updates, lookups


def count_updates():
    inorder_count = 0
    reorder_count = 0
    for update, lookup in zip(updates, lookups):
        for (r1, r2) in rules:
            # Check rules are passed
            p1 = lookup.get(r1, -1)
            if p1 == -1:
                continue
            p2 = lookup.get(r2, -1)
            if p2 == -1:
                continue
            # If they're not:
            if p1 > p2:
                # sort the update by using ruleset
                sorted_update = sorted(update, key=cmp_to_key(compare_rule))
                reorder_count += middle_page(sorted_update)
                break
        else:
            # passed the rules
            inorder_count += middle_page(update)

    return inorder_count, reorder_count


def compare_rule(page1, page2):
    if (page1, page2) in rules:
        return -1
    if (page2, page1) in rules:
        return 1
    return 0


def middle_page(update):
    middle_pos = int(((len(update) + 1) / 2) - 1)
    middle = int(update[middle_pos])
    return middle


rules, updates, lookups = process_input('input.txt')

inorder, reorder = count_updates()

print()
print('In order count  ', inorder)
print('Re-ordered count', reorder)
