# Dec 11 2024 - part 1
file = open('11-1/input.txt')

stones = [int(stone) for stone in file.read().strip().split(' ')]

cache = {
    0: [1]
}

for i in range(25):
    new_stones = []
    for stone in stones:
        if stone in cache:
            new_stones += cache[stone]
            continue
        if len(str(stone)) % 2 == 0:
            mid_point = len(str(stone)) // 2
            new_stone = [int(str(stone)[0:mid_point]), int(str(stone)[mid_point:len(str(stone))])]
        else:
            new_stone = [stone * 2024]
        cache[stone] = new_stone
        new_stones += new_stone
        
    stones = new_stones

print(stones)