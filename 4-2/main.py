# Dec 4 2024 - part 2
file = open('4-2/input.txt')

word = 'MAS'
puzzle_input = []
count = 0
for line in file:
   puzzle_input += [line.rstrip()]

def match_word_in_line(line):
    for i in range(len(line) - len(word) + 1):
        chars = line[i:i+len(word)]
        if chars == word or chars == word[::-1]:
            return True,
    return False

for i in range(1, len(puzzle_input) - 1):
    for j in range(1, len(puzzle_input[i]) - 1):
        if puzzle_input[i][j] == 'A':
            diag_1 = match_word_in_line(puzzle_input[i-1][j-1] + 'A' + puzzle_input[i+1][j+1])
            if not diag_1:
                continue
            diag_2 = match_word_in_line(puzzle_input[i-1][j+1] + 'A' + puzzle_input[i+1][j-1])
            if diag_2:
                count += 1

print(count)