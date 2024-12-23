# Dec 19 2024 - part 2
import copy
from heapq import heappop, heappush
from math import inf

race = []
track = []
with open('20-1/input.txt') as f:
    x = 0
    for line in f:
        y = 0
        row = []
        for char in line.strip():
            if char == 'S' or char == '.':
                track.append((x, y))
            if char == 'E':
                end = (x, y)
            row.append(char)
            y += 1
        race.append(row)
        x += 1

normal_score = len(track)

dimx, dimy = len(race), len(race[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def clear_3x3(race: list[list[int]], center: tuple[int]):
    new_race = copy.deepcopy(race)
    x, y = center
    
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < dimx - 1 and i > 0 and j < dimy - 1 and j > 0:
                new_race[i][j] = '.'
    
    return new_race

def find_best_path(track: list[list[int]], start: tuple[int]):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = dict()
    q = list()
    highscore = inf

    heappush(q, (0, start, 1, [start]))
    while q:
        score, pos, d, path = heappop(q)
        if score > highscore:
            break
        if (pos, d) in visited:
            continue
        visited[(pos, d)] = score
        if pos == end:
            highscore = score
        direction = dirs[d]
        nxt_x, nxt_y = pos[0] + direction[0],  pos[1] + direction[1]
        if track[nxt_x][nxt_y] != "#":
            heappush(q, (score+1, (nxt_x, nxt_y), d, path+[(nxt_x, nxt_y)]))
        heappush(q, (score, pos, (d+1)%4, path))
        heappush(q, (score, pos, (d-1)%4, path))

    return highscore

saved_times = dict()
for track_cell in track:
    normal_time = find_best_path(race, track_cell)
    cheated_track = clear_3x3(race, track_cell)
    cheated_time = find_best_path(cheated_track, track_cell)
    if normal_time == cheated_time:
        continue
    print(track_cell)
    saved_time = normal_time - cheated_time
    if saved_time in saved_times:
        saved_times[saved_time] += 1
    else:
        saved_times[saved_time] = 1
print(saved_times)