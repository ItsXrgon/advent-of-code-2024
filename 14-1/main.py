# Dec 14 2024 - part 1
import re


file = open('14-1/input.txt')

MAP_WIDTH = 101
MAP_HEIGHT = 103

robots = []
top_left_quad = 0
top_right_quad = 0
bot_left_quad = 0
bot_right_quad  = 0

num_regex = r'-?\d+'
for robot in file.read().split('\n'):
    matches = re.findall(num_regex, robot)
    position = [int(value) for value in matches[0:2]]
    velocity = [int(value) for value in matches[2:4]]
    
    robots.append((position, velocity))    

for robot in robots:
    final_x, final_y = robot[0]
    for i in range(100):
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
            
    if final_x > MAP_WIDTH // 2:
        if final_y > MAP_HEIGHT // 2:
            bot_right_quad += 1
        elif final_y < MAP_HEIGHT // 2:
            top_right_quad += 1
    elif final_x < MAP_WIDTH // 2:
        if final_y > MAP_HEIGHT // 2:
            bot_left_quad += 1
        elif final_y < MAP_HEIGHT // 2:
            top_left_quad += 1

print(top_left_quad * top_right_quad * bot_left_quad * bot_right_quad)