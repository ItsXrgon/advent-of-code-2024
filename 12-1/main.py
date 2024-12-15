# Dec 12 2024 - part 1
from collections import defaultdict

file = open('12-1/input.txt')

map = [[char for char in line] for line in file.read().split('\n')]

areas = defaultdict(int)
for i in range(len(map)):
    for j in range(len(map[0])):
