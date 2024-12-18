# Dec 15 2024 - part 1


file = open('15-1/input.txt')
map = []
moves = []
result = 0
player = (0, 0)

map_input, moves_input = file.read().strip().split('\n\n')

x = 0
for row in map_input.split('\n'):
    cells = []
    y = 0
    for col in row.rstrip():
        cells.append(col)
        if col == '@': player = (x, y)
        y += 1
    x += 1
    map.append(cells)

for move in moves_input.strip():
    if move in ['<', '^', '>', 'v']:
        moves.append(move)    

def move_box(location: tuple[int], direction: tuple[int]):
    x, y = location
    if map[x][y] == '.':
        map[x][y] = 'O'
        return True
    
    if map[x][y] == '#': return False
    
    dx, dy = direction
    next_location = (x + dx, y + dy)
    
    return move_box(next_location, direction)

for move in moves:
    if move == '>': direction = (0, 1)
    elif move == '<': direction = (0, -1)
    elif move == '^': direction = (-1, 0)
    else: direction = (1, 0)
        
    x, y = player
    dx, dy = direction
    
    target_location = (x + dx, y + dy)
    tx, ty = target_location
    target_cell = map[tx][ty]
    
    if target_cell == '#': continue
    
    if target_cell == 'O':
        if not move_box(target_location, direction): continue
        map[tx + dx][ty + dy] = 'O'
        
    map[x][y] = '.'
    player = (tx, ty)
    map[tx][ty] = '@'
    
y = 0
for row in map:
    x = 0
    for cell in row:
        if cell == 'O':
            result += (100 * y) + x
        x += 1
    y += 1
print(result)