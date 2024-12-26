# Dec 11 2024 - part 2
from collections import defaultdict

file = open('11-2/input.txt')

stones = [int(stone) for stone in file.read().strip().split(' ')]

def digit_count(num: int):
    return len(str(num))

counter = defaultdict(int)
for n in stones:
    counter[n] += 1

for i in range(75):
    new_counter = defaultdict(int)
    for k, v in counter.items():
        if k == 0:
            new_counter[1] += v
        elif digit_count(k) % 2 == 0:
            n_str = str(k)
            n1 = int(n_str[:int(len(n_str)/2)])
            n2 = int(n_str[int(len(n_str)/2):])
            new_counter[n1] += v
            new_counter[n2] += v
        else:
            new_counter[k * 2024] += v
        
        counter = new_counter

print(sum(counter.values()))