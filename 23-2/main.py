# Dec 23 2024 - part 2

import networkx as nx

with open('23-1/input.txt') as f:
    input_connections  = [connections.split('-') for connections in f.read().split('\n')]
    
G = nx.Graph()
for start,end in input_connections:
    G.add_edge(start, end)
    
cliques = list(nx.find_cliques(G))
cliques = sorted(cliques,key=lambda item:len(item), reverse=True)
biggest_clique = cliques[0]
answer = ','.join(sorted(biggest_clique))
print(answer)