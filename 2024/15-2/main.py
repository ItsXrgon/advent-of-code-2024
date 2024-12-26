# Dec 15 2024 - part 2


file = open('15-2/input.txt')
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
        if col == '@': 
            player = (x, y)
            cells.append('@')
            cells.append('.')
        elif col == '.' or col == '#': 
            cells.append(col)
            cells.append(col)
        elif col == 'O': 
            cells.append('[')
            cells.append(']')
        y += 2
    x += 1
    map.append(cells)

for move in moves_input.strip():
    if move in ['<', '^', '>', 'v']:
        moves.append(move)    
moves = [c for c in moves_input if c != '\n']   

def move_box(location: tuple[int], direction: tuple[int], moving: bool = False):
    x, y = location
    
    if map[x][y] == '.': return True
    if map[x][y] == '#': return False
    
    if map[x][y] == ']':
        c1 = (x, y - 1)
        c2 = (x, y)
    else:
        c1 = (x, y) 
        c2 = (x, y + 1)
        
    c1x, c1y = c1
    c2x, c2y = c2

    dx, dy = direction
    
    can_move = False
    if dx == 0:
        if dy == -1:
            can_move = move_box((c1x, c1y + dy), direction, moving)
            if moving:
                map[c1x][c1y + dy] = map[c1x][c1y]
                map[c1x][c1y] = map[c2x][c2y]
        else:
            can_move = move_box((c2x, c2y + dy), direction, moving)
            if moving:
                map[c2x][c2y + dy] = map[c2x][c2y]
                map[c2x][c2y] = map[c1x][c1y]
    else:
        can_move = move_box((c1x + dx, c1y), direction, moving) and move_box((c2x + dx, c2y), direction, moving)
        if moving:
            map[c1x + dx][c1y] = map[c1x][c1y]
            map[c2x + dx][c2y] = map[c2x][c2y]
            map[c1x][c1y] = '.'
            map[c2x][c2y] = '.'
    return can_move

    

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
    
    if target_cell == '[' or target_cell == ']':
        if not move_box(target_location, direction): continue
        move_box(target_location, direction, True)
                    
    map[x][y] = '.'
    player = (tx, ty)
    map[tx][ty] = '@'
    
y = 0
for row in map:
    x = 0
    for cell in row:
        if cell == '[':
            result += (100 * y) + x
        x += 1
    y += 1
print(result)