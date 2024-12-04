# Dec 3 2024 - part 1
import re

file = open('3-1/input.txt')

program = file.read() 

num_regex = r'-?\d+'

matches = re.findall(f'mul\({num_regex},{num_regex}\)', program)

res = 0
for match in matches:
    num1, num2 = match.replace('mul(', '').replace(')', '').split(',')
    res += int(num1) * int(num2)

print(res)