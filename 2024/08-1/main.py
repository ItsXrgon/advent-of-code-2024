# Dec 8 2024 - part 1
file = open('8-1/input.txt')

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

print(antennas)
for symbol in antennas.keys():
    if len(antennas[symbol]) < 2:
        continue
    for i in range(len(antennas[symbol])):
        for j in range(i + 1, len(antennas[symbol])):
            dx = antennas[symbol][i][0] - antennas[symbol][j][0]
            dy = antennas[symbol][i][1] - antennas[symbol][j][1]
            antinode_1 = (antennas[symbol][i][0] + dx, antennas[symbol][i][1] + dy)
            antinode_2 = (antennas[symbol][j][0] - dx, antennas[symbol][j][1] - dy)
            if antinode_1[0] < x and antinode_1[1] < y and antinode_1[0] >= 0 and antinode_1[1] >= 0:
                antinodes.append(antinode_1)
            if antinode_2[0] < x and antinode_2[1] < y and antinode_2[0] >= 0 and antinode_2[1] >= 0:
                antinodes.append(antinode_2) 
            
print(len(set(antinodes)))