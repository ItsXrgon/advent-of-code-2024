# Dec 5 2024 - part 1
file = open('5-1/input.txt')

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

for update in updates:
    valid = True
    for i in range(len(update)):
        try:
            rules = number_rules_dict[update[i]]
        except:
            rules = []
        for j in range(0, i):
            if update[j] in rules:
                valid = False
                break
    if valid:
        sum += update[len(update) // 2]

print(sum)