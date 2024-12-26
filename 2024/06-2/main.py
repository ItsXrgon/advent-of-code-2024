# Dec 6 2024 - part 1
file = open('6-2/input.txt')

obstacles = []
collisions = []
guard_location = (0, 0)
direction = (0, -1)

attempted_obstacles = []
possible_obstacles = []

y = 0
for line in file:
    x = 0
    map_row = []
    for char in line.rstrip():
        if char == '#':
            obstacles.append((x, y))
        if char == '^':
            guard_location = (x, y)
        x += 1
    y += 1

map_width = y
map_height = x

def get_new_direction(direction: tuple):
    if direction[1] == 1:
        return (-1, 0)
    elif direction[1] == -1:
        return (1, 0)
    elif direction[0] == 1:
        return (0, 1)
    elif direction[0] == -1:
       return  (0, -1)
    
while True:    
    if (guard_location[0] + direction[0], guard_location[1] + direction[1]) in obstacles:
        collisions.append((guard_location, direction))
        direction = get_new_direction(direction)
            
    guard_location =  (guard_location[0] + direction[0], guard_location[1] + direction[1])
    
    if guard_location[0] > map_width - 1 or guard_location[0] < 0 or guard_location[1] > map_height - 1 or guard_location[1] < 0:
        break
    
        
print(len(set(possible_obstacles)))