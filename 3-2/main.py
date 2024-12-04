# Dec 3 2024 - part 2
import re

file = open('3-2/input.txt')

program = file.read() 

num_regex = r'-?\d+'

matches = re.findall(f'mul\({num_regex},{num_regex}\)|do\(\)|don\'t\(\)', program)

res = 0
enabled = True
for match in matches:
    operation = match.split('(')[0]
    if operation == 'do':
        enabled = True
    elif operation == 'don\'t':
        enabled = False 
    elif enabled:
        num1, num2 = match.replace('mul(', '').replace(')', '').split(',')
        res += int(num1) * int(num2)

print(res)