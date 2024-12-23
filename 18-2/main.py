# Dec 18 2024 - part 1

from heapq import heappop, heappush
from math import inf

bytes = []
with open('18-2/input.txt') as f:
    for byte in f:
        x, y = byte.split(',')
        bytes.append((int(x), int(y)))
grid = 70#6
map = [["." for _ in range(grid + 3)] for _ in range(grid + 3)]

for i in range(len(map)):
    map[i][0] = '#'
    map[i][grid+2] = '#'
    map[0][i] = '#'
    map[grid+2][i] = '#'

fallen_bytes = 1024 #12
for byte in bytes[0:fallen_bytes]:
    x, y = byte
    map[y+1][x+1] = '#'

start, end = (1, 1), (grid + 1, grid + 1)
def find_best_path(maze):
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
        if maze[nxt_x][nxt_y] != "#":
            heappush(q, (score+1, (nxt_x, nxt_y), d, path+[(nxt_x, nxt_y)]))
        heappush(q, (score, pos, (d+1)%4, path))
        heappush(q, (score, pos, (d-1)%4, path))

    return highscore

for byte in bytes[fallen_bytes:]:
    x, y = byte
    map[y+1][x+1] = '#'
    if find_best_path(map) == inf:
        print(byte)
        break