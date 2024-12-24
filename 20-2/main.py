# Dec 20 2024 - part 2

race = []
with open('20-2/input.txt') as f:
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
    
    for nidx in range(tidx + 3, len(track)):
        neighbor = track[nidx]
        nx, ny = neighbor
        dx, dy = (tx - nx, ty - ny)
        moves_made = abs(dx) + abs(dy)
        if moves_made <= 20:
            neighbors.append(nidx)
    
    for nidx in neighbors:     
        neighbor = track[nidx]
        
        nx, ny = neighbor
        dx, dy = (tx - nx, ty - ny)
        moves_made = abs(dx) + abs(dy)
    
        new_time = normal_time - nidx + tidx + moves_made
        
        if normal_time - new_time >= 100:
            cheats += 1

print(cheats)