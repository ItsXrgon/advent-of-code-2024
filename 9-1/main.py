# Dec 9 2024 - part 1
file = open('9-1/input.txt')

checksum = 0
disk_map = []
i = 0
for char in file.read():
    count = int(char)
    if i % 2 == 0:
        value = str(int(i / 2))
    else:
        value = '.'
    for _ in range(count): 
        disk_map.append(value)
    i += 1  

start, end = 0, len(disk_map) - 1

while start <= end:
    if disk_map[start] != '.':
        value = int(disk_map[start])
    else:
        while disk_map[end] == '.':
            end -= 1
        value =  int(disk_map[end])
        end -= 1
    checksum += value * start
    start += 1

print(checksum)
