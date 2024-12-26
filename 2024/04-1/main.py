# Dec 4 2024 - part 1
file = open('4-1/input.txt')

word = 'XMAS'
puzzle_input = []
for line in file:
   puzzle_input += [line.rstrip()]

width = max(len(puzzle_input), len(puzzle_input[0]))
height = min(len(puzzle_input), len(puzzle_input[0]))
count = 0

def count_word_in_line(line):
    count = 0
    for i in range(len(line) - len(word) + 1):
        chars = line[i:i+len(word)]
        if chars == word or chars == word[::-1]:
            count += 1
        
    return count

def count_horizontal():
    count = 0
    for i in range(len(puzzle_input)):
        count += count_word_in_line(puzzle_input[i])
    return count

def count_vertical():
    count = 0
    for i in range(width):
        count += count_word_in_line(''.join([puzzle_input[j][i] for j in range(height)]))   
    return count

def count_diagonal():
    count = 0
    
    for i in range(width, -1, -1):
        line = ''
        j = 0
        while i+j < width:
            line += puzzle_input[j][i+j]
            j += 1
        count += count_word_in_line(line)
    
    for i in range(1, height):
        line = ''
        j = 0
        while i+j < height:
            line += puzzle_input[i+j][j]
            j += 1
        count += count_word_in_line(line)
    
    puzzle_input.reverse()
    
    for i in range(width, -1, -1):
        line = ''
        j = 0
        while i+j < width:
            line += puzzle_input[j][i+j]
            j += 1
        count += count_word_in_line(line)
    
    for i in range(1, height):
        line = ''
        j = 0
        while i+j < height:
            line += puzzle_input[i+j][j]
            j += 1
        count += count_word_in_line(line)
        
    return count


count += count_horizontal()
count += count_vertical()
count += count_diagonal()

print(count)