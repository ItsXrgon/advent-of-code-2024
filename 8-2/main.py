# Dec 8 2024 - part 2
file = open('8-2/input.txt')

antennas = {}
antinodes = []
y = 0
for line in file:
    x = 0
    for char in line.rstrip():
        if char != '.':
            if char in antennas:
                antennas[char].append((x, y))
            else:
                antennas[char] = [(x, y)]
        x += 1
    y += 1

for symbol in antennas.keys():
    if len(antennas[symbol]) < 2:
        continue
    for i in range(len(antennas[symbol])):
        for j in range(i + 1, len(antennas[symbol])):
            print(antennas[symbol][j])
            antinodes.append(antennas[symbol][i])
            dx = antennas[symbol][i][0] - antennas[symbol][j][0]
            dy = antennas[symbol][i][1] - antennas[symbol][j][1]
            
            startx, starty = antennas[symbol][i]
            while startx >= 0 and starty >= 0 and startx < x and starty < y:
                antinodes.append((startx, starty))
                startx, starty = startx - dx, starty - dy
            
            startx, starty = antennas[symbol][i]
            while startx >= 0 and starty >= 0 and startx < x and starty < y:
                antinodes.append((startx, starty))
                startx, starty = startx + dx, starty + dy
                
print(len(set(antinodes)))