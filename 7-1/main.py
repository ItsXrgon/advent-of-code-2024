# Dec 7 2024 - part 1
file = open('7-1/input.txt')

sum = 0
tests = []
for line in file:
    result, test_data = line.strip().split(':')
    test_values = [int(value) for value in test_data.strip().split(' ')]
    
    tests.append((int(result), test_values)) 

def evaluate_symbol(goal, current_value, rest):
    if len(rest) == 0:
        return goal == current_value
    
    if current_value > goal:
        return False

    add_value = current_value + rest[0]
    mul_value = current_value * rest[0]
    
    if len(rest) == 1:
       return add_value == goal or mul_value == goal
    else:
        return evaluate_symbol(goal, add_value, rest[1:]) or evaluate_symbol(goal, mul_value, rest[1:])

for test in tests:
    if evaluate_symbol(test[0], 0, test[1]):
        sum += test[0]

print(sum)