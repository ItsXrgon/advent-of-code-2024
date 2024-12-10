# Dec 9 2024 - part 2
file = open('9-2/input.txt')

checksum = 0
disk_map = []
file_sizes = []
gap_sizes = []
i = 0
for char in file.read():
    count = int(char)
    if i % 2 == 0:
        value = int(i / 2)
        file_sizes.append((len(disk_map), count))
    else:
        value = '.'
        gap_sizes.append((len(disk_map), count))
    for _ in range(count): 
        disk_map.append(value)
    i += 1  
    
file_sizes.reverse()
for file in file_sizes:
    for gap in gap_sizes:
        if file[1] <= gap[1] and gap[0] <= file[0]:
            for j in range(file[1]):
                disk_map[gap[0] + j] = disk_map[file[0] + j]
                disk_map[file[0] + j] = '.'
            gap_left = gap[1] - file[1]
            if gap_left > 0:
                gap_idx = gap_sizes.index(gap)
                gap_sizes[gap_idx]= (gap[0] + file[1], gap_left)
            else:
                gap_sizes.remove(gap)
            break
            
for i in range(len(disk_map)):
    if disk_map[i] != '.': 
        checksum += i * int(disk_map[i])

print(checksum)
