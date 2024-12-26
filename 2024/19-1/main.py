# Dec 19 2024 - part 1

towels = []
patterns = []
possible_designs = 0
with open('19-1/input.txt') as f:
    towels_input, patterns_input = f.read().split('\n\n')
    towels = towels_input.split(', ')
    
    patterns = patterns_input.split('\n')

def check_pattern(pattern: str, failed_patterns: list) -> int:
    if len(pattern) == 0:
        return 1
    
    if pattern in failed_patterns:
        return 0
    
    for towel in towels:
        if pattern[0:len(towel)] == towel:
            new_pattern = pattern[len(towel):]
            if check_pattern(new_pattern, failed_patterns):
                return 1
            else: failed_patterns.append(new_pattern)
    return 0
    
for pattern in patterns:
    possible_designs += check_pattern(pattern, [])
    
print(possible_designs)