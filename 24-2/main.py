# Dec 24 2024 - part 2

values = dict()
connections = dict()
binary = []
x_bin = []
y_bin = []

with open('24-2/input.txt') as f:
    starting_values, input_gates  = f.read().split('\n\n')
    
    for starting_value in starting_values.split('\n'):
        variable, value = starting_value.split(': ')
        values[variable] = int(value)
        
        if variable[0] == 'x':
            x_bin.append(value)
        if variable[0] == 'y':
            y_bin.append(value)
    x_bin.reverse()
    y_bin.reverse()     
    for input_gate in input_gates.split('\n'):
        input, output_key = input_gate.split(' -> ')
        var1, gate, var2 = input.split(" ")
        connections[output_key] = {
            "variables": [var1, var2], 
            "gate": gate,
        }
        if output_key[0] == 'z':
            binary.append(-1)

x = int("".join(x_bin), 2)
y = int("".join(y_bin), 2)
z = x + y

def solve_connection(connection: dict):
    gate = connection['gate']
    var1, var2 = connection['variables']
    var1_value = var1_value = -1
    if var1 in values:
        var1_value = values[var1]
    else:
        var1_value = solve_connection(connections[var1])
    if var2 in values:
        var2_value = values[var2]
    else:
        var2_value = solve_connection(connections[var2])
    
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
                
    values[output_key] = result
    return result

for z_connection in connections:
    if z_connection[0] != 'z':
        continue
    index = int(z_connection.replace('z', ''))
    binary[index] = str(solve_connection(connections[z_connection]))
binary.reverse()
print(bin(z).removeprefix('0b'))
print("".join(binary))