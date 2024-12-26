# Dec 14 2024 - part 2
from collections import defaultdict
import re
from matplotlib import pyplot as plt
import numpy as np

file = open('14-2/input.txt')

MAP_WIDTH = 101
MAP_HEIGHT = 103

robots = []
final_robots = []

num_regex = r'-?\d+'
for robot in file.read().split('\n'):
    matches = re.findall(num_regex, robot)
    position = [int(value) for value in matches[0:2]]
    velocity = [int(value) for value in matches[2:4]]
    
    robots.append((position, velocity))    

def plot_map(cycle: int):
    coords = defaultdict(int)
    for robot in final_robots:
        coords[robot] += 1

    bitmap = np.zeros((MAP_HEIGHT,MAP_WIDTH), dtype=np.uint8)

    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if (x, y) in coords:
                bitmap[y][x] = 0
            else:
                bitmap[y][x] = 255

    plt.imshow(bitmap)
    plt.axis("off")
    plt.imsave(f"14-2/outputs/{cycle}.png", bitmap)
    
for i in range(0, 999999):
    final_robots = []
    for robot in robots:
        final_x, final_y = robot[0]
    
        delta_x, delta_y = robot[1]
        
        final_x += delta_x
        final_y += delta_y
        
        if final_x >= MAP_WIDTH:
            final_x = final_x - MAP_WIDTH
            
        if final_x < 0:
            final_x = MAP_WIDTH + final_x
        
        if final_y >= MAP_HEIGHT:
            final_y = final_y - MAP_HEIGHT
        
        if final_y < 0:
            final_y = MAP_HEIGHT + final_y
            
        final_robots.append((final_x, final_y))

    plot_map(i)