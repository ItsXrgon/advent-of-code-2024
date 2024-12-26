# Dec 5 2024 - part 2
file = open('5-2/input.txt')

number_rules_dict = {}
updates = []
sum = 0
[rules, input_updates] = file.read().split('\n\n')
for rule in rules.split('\n'):
    number, rule = rule.split('|')
    if int(number) in number_rules_dict:
        number_rules_dict[int(number)].append(int(rule))
    else:
        number_rules_dict[int(number)] = [int(rule)]
        
for input_update in input_updates.split('\n'):
    update = [int(update) for update in input_update.split(',')]
    updates.append(update)

def bubble_sort(update):
    swapped = False
    
    for i in range(len(update) - 1):
        try:
            rules = number_rules_dict[update[i]]
        except:
            rules = []
        if update[i+1] in rules:
            update[i+1], update[i] = update[i], update[i+1]
            swapped = True
    if swapped:
        return bubble_sort(update)
    
    return update

for update in updates:
    valid = True
    i = 0
    for i in range(len(update)):
        if not valid:
            sum += bubble_sort(update)[len(update) // 2]
            break
        try:
            rules = number_rules_dict[update[i]]
        except:
            rules = []
        for j in range(0, i):
            if update[j] in rules:
                valid = False
                break

print(sum)