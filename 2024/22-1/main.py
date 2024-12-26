# Dec 22 2024 - part 1

from math import floor

with open('22-1/input.txt') as f:
    numbers  = [int(num) for num in f.read().split('\n')]

stage1_cache = dict()
stage2_cache = dict()
stage3_cache = dict()

results = []

for number in numbers:
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
        
    results.append(number)
            
print(sum(results))