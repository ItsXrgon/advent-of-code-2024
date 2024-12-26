# Dec 22 2024 - part 2

from math import floor

import numpy as np


with open('22-2/input.txt') as f:
    numbers  = [int(num) for num in f.read().split('\n')]

stage1_cache = dict()
stage2_cache = dict()
stage3_cache = dict()

monkeynomics = dict()

for number in numbers:
    sequence = np.zeros(2001, dtype = int)
    sequence[0] = number % 10
    monkey_sequences = set()
    for i in range(2000):
        if number in stage1_cache:
            stage1 = stage1_cache[number]
        else:
            stage1 = ((number * 64) ^ number) % 16777216
            stage1_cache[number] = stage1
        number = stage1
        
        if number in stage2_cache:
            stage2 = stage2_cache[number]
        else:
            stage2 = (floor(stage1 / 32) ^ stage1) % 16777216
            stage2_cache[number] = stage2
        number = stage2
        
        if number in stage3_cache:
            stage3 = stage3_cache[number]
        else:
            stage3 = ((stage2 * 2048) ^ stage2) % 16777216
            stage3_cache[number] = stage3
        number = stage3
        
        sequence[i+1] = number % 10
        
    differences = np.diff(sequence)

    for j in range(4, len(differences)): 
        hash = str(differences[j-3:j+1])
        if hash in monkey_sequences:
            continue 
        monkey_sequences.add(hash)
        if hash in monkeynomics:
            monkeynomics[hash] += sequence[j + 1]
        else:
            monkeynomics[hash] = sequence[j + 1]
        
        
max = max(monkeynomics.values())
print(max)
# < 2041