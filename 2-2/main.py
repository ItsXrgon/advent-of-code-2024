# Dec 2 2024 - part 2
file = open('2-2/input.txt')

count = 0

def check_validity(levels, tolerate):
    levels_div = [lj-li for li, lj in zip(levels, levels[1:])]
    increasing = [diff > 0 and diff < 4 for diff in levels_div]
    decreasing = [diff < 0 and diff > -4 for diff in levels_div]
    if all(increasing) or all(decreasing):
        return True
    elif not tolerate:
        for i, level in enumerate(levels):
            tolerated_report = level[:]
            del tolerated_report[i]
            if check_validity(tolerated_report, True):
                return True
    return False

for line in file:
    levels = [int(level) for level in line.rstrip().split(" ")]
    if check_validity(levels, False):
        count += 1
    
print(count)