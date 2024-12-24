from itertools import permutations
import numpy as np
# Dec 21 2024 - part 1

numeric_keypad = {
    'A': (3, 2),
    '0': (3, 1),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '4': (1, 1),
    '5': (1, 2),
    '6': (1, 3),
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
}

direction_keypad = {
    'A': (0, 2),
    '^': (0, 1),
    '>': (1, 2),
    'v': (1, 1),
    '<': (1, 0),
}

codes = []

with open('21-1/input.txt') as f:
    codes = f.read().split('\n')

def append_keypad_possibilities(possibilities: list[str], delta: tuple[int], start: tuple[int], illegals: dict[tuple[int], str]) -> list[str]:
    new_possibilities = []

    dx, dy = delta
    x_move, y_move = '', ''
    if dx > 0:
        x_move = 'v'
    else:
        x_move = '^'
        
    if dy > 0:
        y_move = '>'
    else:
        y_move = '<'
    
    codes = x_move * abs(dx) + y_move * abs(dy)
    
    for illegal in illegals:
        if start == illegal:
            illegal_code = illegals[illegal]
            codes = list(filter(lambda k: ''.join(k[0:len(illegal_code)]) != illegal_code, codes))
            
    if len(possibilities) == 0:
        new_possibilities = ["".join(char for char in code) + 'A' for code in codes]
    else:
        for possibility in possibilities:
            possibility_chars = "".join(char for char in possibility)
            for code in codes:
                code_chars = "".join(char for char in code)
                new_possibilities.append(possibility_chars + code_chars + 'A')
            
    return new_possibilities

def get_numeric_keypad_presses(code: str): 
    current = numeric_keypad['A']
    possibilities = []
    
    illegals = {
        numeric_keypad['1']: 'v',
        numeric_keypad['2']: 'vv',
        numeric_keypad['7']: 'vvv',
        numeric_keypad['0']: '<',
        numeric_keypad['A']: '<<',
    }
    
    for char in code:
        target = numeric_keypad[char]
        cx, cy = current
        tx, ty = target
        
        delta = (tx - cx, ty - cy)
        possibilities = append_keypad_possibilities(possibilities, delta, current, illegals)
        current = target
    return possibilities

def get_direction_keypad_presses(code: str): 
    current = direction_keypad['A']
    possibilities = []
    
    illegals = {
        direction_keypad['<']: '^',
        direction_keypad['^']: '<',
        direction_keypad['A']: '<<',
    }
    
    for char in code:
        target = direction_keypad[char]
        cx, cy = current
        tx, ty = target
        
        delta = (tx - cx, ty - cy)
        possibilities = append_keypad_possibilities(possibilities, delta, current, illegals)
        current = target
    return possibilities

keypad_results = get_numeric_keypad_presses('029A')
results = keypad_results
for _ in range(3):
    new_results = []
    for result in results:
        new_results += get_direction_keypad_presses(result)
    new_results = list(set(new_results))
    new_results.sort(key=lambda s: len(s))
    new_results = list(filter(lambda s: len(s) == len(new_results[0]), new_results))
    print(new_results)
    results =  new_results
    
print(results)