# Dec 13 2024 - part 1
import re


file = open('13-1/input.txt')

A_COST = 3
B_COST = 1

machines = []
results = []
num_regex = r'-?\d+'
for machine in file.read().split('\n\n'):
    matches = re.findall(num_regex, machine)
    deltaA = [int(value) for value in matches[0:2]]
    deltaB = [int(value) for value in matches[2:4]]
    prize = [int(value) for value in matches[4:6]]
    
    machines.append((deltaA, deltaB, prize))    

for machine in machines:
    delta_a_x, delta_a_y = machine[0]
    delta_b_x, delta_b_y = machine[1]
    prize_x, prize_y = machine[2]

    # prize_x = delta_a_x * a_presses + delta_b_x * b_presses
    # prize_y = delta_a_y * a_presses + delta_b_y * b_presses
    
    
    a_presses, remainder = divmod(prize_x * delta_b_y - prize_y * delta_b_x, delta_a_x * delta_b_y - delta_a_y * delta_b_x)
    
    if remainder: # not an int
        continue

    b_presses, remainder = divmod(prize_x - delta_a_x * a_presses, delta_b_x)

    if remainder: # not an int
        continue
    
    results.append(b_presses * B_COST + a_presses * A_COST)
            
print(sum(results))