# Dec 20 2024 - part 1

race = []
with open('20-1/input.txt') as f:
    x = 0
    for line in f:
        y = 0
        row = []
        for char in line.strip():
            if char == 'S':
                start = (x, y)
            if char == 'E':
                end = (x, y)
            row.append(char)
            y += 1
        race.append(row)
        x += 1

dimx, dimy = len(race), len(race[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def run_race(track: list[list[int]], start: tuple[int]):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    path = [start]
    cell = start
    direction = 0

    while cell != end:
        cx, cy = cell
        dx, dy = dirs[direction]
        next = (cx + dx, cy + dy)
        if track[next[0]][next[1]] != '#' and next not in path:
            path.append(next)
            cell = next
            continue
        direction = (direction + 1) % 4

    return path

track = run_race(race, start)
normal_time = len(track)
cheats = 0
for tidx in range(len(track)):
    track_cell = track[tidx]
    tx, ty = track_cell
    neighbors = []
    
    for x in range(-2, 3):
        for y in range(-2 + abs(x), 2 - abs(x) + 1):
            new_cell = (tx + x, ty + y)
            try: 
                if race[tx + x][ty + y] != '#':
                    neighbors.append(track.index(new_cell))
            except:
                continue
    
    for nidx in neighbors:     
        if nidx - 3 <= tidx: continue # not worth cheating
        
        neighbor = track[nidx]
        
        nx, ny = neighbor
        dx, dy = (tx - nx, ty - ny)
        moves_made = abs(dx) + abs(dy)
        
        new_time = normal_time - nidx + tidx + moves_made
        #print('cheating from', track_cell, "to", neighbor, "benefit", normal_time - new_time)
        if normal_time - new_time >= 100:
            cheats += 1

print(cheats)