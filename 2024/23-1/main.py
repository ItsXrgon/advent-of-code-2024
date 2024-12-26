# Dec 23 2024 - part 1

from collections import defaultdict


connections = defaultdict(list)

with open('23-1/input.txt') as f:
    input_connections  = [connections.split('-') for connections in f.read().split('\n')]
    
for connection in input_connections:
    pc1, pc2 = connection
    
    connections[pc1].append(pc2)
    connections[pc2].append(pc1)

sets = set()
for pc1 in connections:
    for pc2 in connections[pc1]:
        both = []
        for pc3 in connections[pc2]:
            if pc3 in connections[pc1]:
                both.append(sorted([pc1, pc2, pc3]))
                
        for matches in both:
            for pc in matches:
                if pc[0] == 't':
                    sets.add(tuple(matches))
                    break

print(len(sets))
    