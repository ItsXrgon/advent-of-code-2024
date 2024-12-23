# Dec 16 2024 - part 1

from heapq import heappop, heappush
from math import inf

maze = []
with open('16-1/input.txt') as f:
    x = 0
    for line in f:
        y = 0
        row = []
        for char in line:
            if char == 'S':
                start = (x, y)
            if char == 'E':
                end = (x, y)
            row.append(char)
            y += 1
        maze.append(row)
        x += 1 
dimx, dimy = len(maze), len(maze[0])
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

visited = dict()
q = list()
highscore = inf
paths = list()

heappush(q, (0, start, 1, ""))
while q:
    score, pos, d, path = heappop(q)
    if score > highscore:
        break
    if (pos, d) in visited and visited[(pos, d)] < score:
        continue
    visited[(pos, d)] = score
    if pos == end:
        highscore = score
        paths.append(path)
    direction = dirs[d]
    if maze[pos[0] + direction[0]][pos[1] + direction[1]] != "#":
        heappush(q, (score+1, (pos[0] + direction[0], pos[1] + direction[1]), d, path+"F"))
    heappush(q, (score+1000, pos, (d+1)%4, path+"R"))
    heappush(q, (score+1000, pos, (d-1)%4, path+"L"))

tiles = set()
tiles.add(start)
for p in paths:
    t, d = (start, 1)
    for c in p:
        if c=="L": d=(d-1)%4
        elif c=="R": d=(d+1)%4
        elif c=="F":
            t+=dirs[d]
            tiles.add(t)

print(highscore)