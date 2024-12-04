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
    
    for i in range(len(levels) - 2):
        if not check_validity(levels[i], levels[i+1]) or not check_validity(levels[i+1], levels[i+2]):
            safe = False
            break 
        if levels[i] > levels[i + 1] and not levels[i+1] > levels[i + 2]:
            safe = False
            break
        if levels[i] < levels[i + 1] and not levels[i+1] < levels[i + 2]:
            safe = False
            break
    if safe:
        count += 1
    
print(count)