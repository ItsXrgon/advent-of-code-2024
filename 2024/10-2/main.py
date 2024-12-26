# Dec 10 2024 - part 2
file = open('10-2/input.txt')

map = []
trailheads = []
score = 0
y = 0
for line in file:
    row = []
    x = 0
    for num in line.rstrip():
        row.append(int(num))
        if int(num) == 0:
            trailheads.append((x, y))
        x += 1
    y+=1
    map.append(row)

width = len(map)
height = len(map[0])

def get_trailhead_score(location: tuple, value: int, nines: list):
    if map[location[1]][location[0]] == 9:
        nines.append(location)
        return
    
    up = (location[0], location[1] - 1)
    down = (location[0], location[1] + 1)
    right = (location[0] + 1, location[1])
    left = (location[0] - 1, location[1])
    
    up_valid = up[1] >= 0 and map[up[1]][up[0]] == value + 1
    down_valid = down[1] < width and map[down[1]][down[0]] == value + 1
    right_valid = right[0] < height and map[right[1]][right[0]] == value + 1
    left_valid = left[0] >= 0 and map[left[1]][left[0]] == value + 1
    
    if up_valid:
        get_trailhead_score(up, value + 1, nines)
    if down_valid:
        get_trailhead_score(down, value + 1, nines)
    if right_valid:
        get_trailhead_score(right, value + 1, nines)
    if left_valid:
        get_trailhead_score(left, value + 1, nines)


for trailhead in trailheads:
    nines = []
    get_trailhead_score(trailhead, 0, nines)
    score += len(nines)
print(score)