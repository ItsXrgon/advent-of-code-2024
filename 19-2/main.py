# Dec 19 2024 - part 2

towels = []
patterns = []
possible_designs = 0
with open('19-2/input.txt') as f:
    towels_input, patterns_input = f.read().split('\n\n')
    towels = towels_input.split(', ')
    
    patterns = patterns_input.split('\n')

cache = dict()
total_count = 0
def check_pattern(pattern: str) -> int:
    if len(pattern) == 0:
        return 1
    
    global cache
    count = 0
    for towel in towels:
        if pattern[0:len(towel)] == towel:
            new_pattern = pattern[len(towel):]
            if new_pattern not in cache:
                new_val = check_pattern(new_pattern)
                cache[new_pattern] = new_val
            count += cache[new_pattern]
    return count
    
for pattern in patterns:
    cache = dict()
    total_count += check_pattern(pattern)
    
print(total_count)