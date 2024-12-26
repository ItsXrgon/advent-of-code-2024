# Dec 17 2024 - part 1

import re
num_regex = r'-?\d+'

reg_a = 0
reg_b = 0
reg_c = 0
instructions = []
out = ""

with open('17-1/input.txt') as file:
    registers_input, instructions_input = file.read().split('\n\n')
    nums = [int(num.replace(': ', '')) for num in re.findall(f': {num_regex}', registers_input)]
    reg_a = nums[0]
    reg_b = nums[1]
    reg_c = nums[2]
    
    instructions = [(int(opcode), int(operand)) for inst in re.findall(f'{num_regex},{num_regex}', instructions_input) for opcode, operand in [inst.split(',')]]

def get_combo_operand(operand: int):
    if operand < 4:
        return operand

    return [reg_a, reg_b, reg_c][operand - 4]

i = 0
while i < len(instructions):
    opcode, operand = instructions[i]
    
    skip_inc = False
    
    if opcode == 0:
        reg_a = reg_a // 2 ** get_combo_operand(operand)
    elif opcode == 1:
        reg_b = reg_b ^ operand
    elif opcode == 2:
        reg_b = get_combo_operand(operand) % 8
    elif opcode == 3:
        if reg_a != 0:
            i = operand // 2
            skip_inc = True
    elif opcode == 4:
        reg_b = reg_b ^ reg_c
    elif opcode == 5:
        out += str(get_combo_operand(operand) % 8) + ','
    elif opcode == 6:
        reg_b = reg_a // 2 ** get_combo_operand(operand)
    elif opcode == 7:
        reg_c = reg_a // 2 ** get_combo_operand(operand)
    
    if not skip_inc:
        i += 1
print(out)