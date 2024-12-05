from functools import cmp_to_key


def process_input(filename):
    """Acquire input data"""
    # get lines
    with open(filename) as file:
        input = file.read().splitlines()

    # Initialise Data Structures
    rules = []  # list[tuple()]
    updates = []  # list[tuple()]
    lookups = []  # list[dict{}]

    # Get data into vars
    for line in input:
        # Ignore blank line
        if line == '':
            continue
        # If it's a rule
        if '|' in line:
            rule = line.split('|')
            rules.append(tuple(rule))
        # If it's an update
        else:
            update = line.split(',')
            if len(update) > 0:
                updates.append(tuple(update))

    # Store the updates in as dictionaries for easy lookup
    # For each update, make a dictionary{page:indexOfPage}
    for update in updates:
        lookup = {}
        for p, page in enumerate(update):
            lookup[page] = p
        lookups.append(lookup)

    return rules, updates, lookups


def count_updates():
    # Initialise counts
    pt1 = 0
    pt2 = 0

    # Loop through the updates and lookups, use zip() to get both update and lookup value
    for update, lookup in zip(updates, lookups):
        # Loop through the rules, use (r1, r2)
        for (r1, r2) in rules:
            # They're relevant if the lookup has a value for both numbers of the rule
            index1 = lookup.get(r1, -1)
            index2 = lookup.get(r2, -1)
            if index1 == -1:
                continue
            if index2 == -1:
                continue
            # If they are relevant, but they are wrong order, the update needs sorting
            if index1 > index2:
                # sort the update by using custom ruleset
                sortedUpdate = sorted(update, key=cmp_to_key(compare_rule))
                # find the middle page and add to part 2
                pt2 += middle_page(sortedUpdate)
                # Finished with this rule so break
                break
        # This runs if the update is correct
        else:
            pt1 += middle_page(update)

    return pt1, pt2


def compare_rule(page1, page2):
    # Custom comparison
    # If it's in rules, return -1
    if (page1, page2) in rules:
        return -1
    # If it's in rules backwards, return 1
    if (page2, page1) in rules:
        return 1
    # If it's not in rules, return 0
    return 0


def middle_page(update):
    # return middle page of an update
    middle_pos = int(((len(update) + 1) / 2) - 1)
    middle = int(update[middle_pos])
    return middle


rules, updates, lookups = process_input('input.txt')

p1, p2 = count_updates()

print('Part 1', p1)
print('part 2', p2)
