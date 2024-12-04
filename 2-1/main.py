# Dec 2 2024 - part 1
file = open('2-1/input.txt')

count = 0

def check_validity(num1, num2):
    diff = abs(num1 - num2)
    if diff < 1 or diff > 3:
        return False
    return True

for line in file:
    levels = [int(level) for level in line.split(" ")]

    safe = True
    
    levels_div = [lj-li for li, lj in zip(levels, levels[1:])]
    increasing = [diff > 0 and diff < 4 for diff in levels_div]
    decreasing = [diff < 0 and diff > -4 for diff in levels_div]
    
    if all(increasing) or all(decreasing):
        count += 1
    
print(count)