# Dec 14 2024 - part 1
import re
# FAILED ATTEMPT 
# FAILED ATTEMPT
# FAILED ATTEMPT

file = open('14-1/input.txt')

MAP_WIDTH = 11
MAP_HEIGHT = 7

robots = []
final_robots = []
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
    total_delta_x = robot[1][0] * 5 # total movement in x direction (ignoring looping around map) 
    total_delta_y = robot[1][1] * 5 # total movement in y direction (ignoring looping around map)
    
    delta_x = total_delta_x % MAP_WIDTH  # total movement in x direction but removing loops
    delta_y = total_delta_y % MAP_HEIGHT # total movement in y direction but removing loops
    
    final_x = robot[0][0] + delta_x # final x location
    final_y = robot[0][1] + delta_y # final y location
    
    if final_x >= MAP_WIDTH:
        final_x = final_x - MAP_WIDTH
        
    if final_x < 0:
        final_x = MAP_WIDTH - 1 + final_x
    
    if final_y >= MAP_HEIGHT:
        final_y = final_y - MAP_HEIGHT
    
    if final_y < 0:
        final_y = MAP_HEIGHT - 1 + final_y
    
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
            
    final_robots.append((final_x, final_y))
    
    print(final_x, final_y)

for i in range(MAP_HEIGHT):
    for j in range(MAP_WIDTH):
        robot_count = 0
        for robot in final_robots:
            if robot[0] == j and robot[1] == i:
                robot_count += 1
        if robot_count == 0:
            print('.', end='')
        else:
            print(robot_count, end='')
    print()
            
print(top_left_quad, top_right_quad, bot_left_quad, bot_right_quad)
# start p=2,4 & end p = 1,3
# 4 -> 1 -> 5 -> 2 -> 6 -> 3
# y: 0 -> 5 -> 2 -> 7 -> 4 -> 1
# x: 0 -> 2 -> 4 -> 6 -> 8 -> 10