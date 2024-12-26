# Dec 25 2024 - part 1

locks = []
keys = []
with open('25-1/input.txt') as f:
    schematics = f.read().split('\n\n')
    for schema in schematics:
        rows = schema.split('\n')
        heights = [-1] * 5
        is_lock = False
        for i in range(len(rows)):
            row = rows[i]
            for j in range(len(row)):
                if i == 0 and j == 0 and row[j] == '#':
                    is_lock = True
                if row[j] == '#':
                    heights[j] += 1
        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)
matches = 0
for key in keys:
    for lock in locks:
        matched = True
        for i in range(5):
            if lock[i] + key[i] >= 6:
                matched = False
        if matched:
            matches += 1
print(matches)