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
wrong = set()
def solve_connection(connection_key: str, connections: dict):
    connection = connections[connection_key]
    gate = connection['gate']
    var1, var2 = connection['variables']
    var1_value = var1_value = -1
    
    if var1 in values:
        var1_value = values[var1]
    else:
        var1_value = solve_connection(var1, connections)
    if var2 in values:
        var2_value = values[var2]
    else:
        var2_value = solve_connection(var2, connections)
            
    result = -1
    if connection_key[0] == "z" and gate != "XOR" and connection_key != "z45":
        wrong.add(connection_key)
    if (
        gate == "XOR"
        and connection_key[0] not in ["x", "y", "z"]
        and var1[0] not in ["x", "y", "z"]
        and var2[0] not in ["x", "y", "z"]
    ):
        wrong.add(connection_key)    
    if gate == "AND" and "x00" not in [var1, var2]:
        for subkey in connections:
            subconnection = connections[subkey]
            subgate = subconnection['gate']
            subvar1, subvar2 = subconnection['variables']
            if (connection_key == subvar1 or connection_key == subvar2) and subgate != "OR":
                wrong.add(connection_key)
    if gate == "XOR":
        for subkey in connections:
            subconnection = connections[subkey]
            subgate = subconnection['gate']
            subvar1, subvar2 = subconnection['variables']
            if (connection_key == subvar1 or connection_key == subvar2) and subgate == "OR":
                wrong.add(connection_key)    
                
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
                
    return result

def solve_connections(connections: dict):
    for z_connection in connections:
        if z_connection[0] != 'z':
            continue
        index = int(z_connection.replace('z', ''))
        result = solve_connection(z_connection, connections)
        binary[index] = str(result)

solve_connections(connections)
binary.reverse()

print(",".join(sorted(wrong)))

def get_path(key: str):
    if key[0] == 'x' or key[0] == 'y':
        return []
    variables = connections[key]['variables']
    gate = connections[key]['gate']
    if len(variables) == 0: return [key]
    
    var1, var2 = variables
    return [(var1, gate, var2, key)] + get_path(var1) + get_path(var2)