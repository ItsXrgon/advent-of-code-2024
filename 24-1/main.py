# Dec 24 2024 - part 1

values = dict()
connections = dict()
binary = []
with open('24-1/input.txt') as f:
    starting_values, input_gates  = f.read().split('\n\n')
    
    for starting_value in starting_values.split('\n'):
        variable, value = starting_value.split(': ')
        values[variable] = int(value)
        
    for input_gate in input_gates.split('\n'):
        input, output = input_gate.split(' -> ')
        var1, gate, var2 = input.split(" ")
        connections[output] = {
            "variables": [var1, var2], 
            "gate": gate,
        }
        if output[0] == 'z':
            binary.append(-1)
                    
while True:
    all_z_found = True
    for output in connections:
        if output in values:
            continue
        connection = connections[output]
        gate = connection['gate']
        var1, var2 = connection['variables']
        var1_value = var1_value = -1
        if var1 in values:
            var1_value = values[var1]
        if var2 in values:
            var2_value = values[var2]
        
        result = -1
        if gate == 'AND':
            if var1_value == 0 or var2_value == 0:
                result = 0
            elif var1_value == 1 and var2_value == 1:
                result = 1
                
        if gate == 'OR':
            if var1_value == 1 or var2_value == 1:
                result = 1
            elif var1_value == 0 and var2_value == 0:
                result = 0
                
        if gate == 'XOR':
            if var1_value != -1 and var2_value != -1:
                if var1_value == var2_value:
                    result = 0
                else:
                    result = 1
                    
        if result != -1:
            values[output] = result 
        elif output[0] == 'z':
            all_z_found = False
            
    if all_z_found:
        break

for value in values:
    if value[0] == 'z':
        index = int(value.replace('z', ''))
        binary[index] = str(values[value])
binary.reverse()

print(int("".join(binary), 2))
    
# < 53624194074598
# > 35495193363686