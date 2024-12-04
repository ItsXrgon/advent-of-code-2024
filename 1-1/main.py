# Dec 1 2024 - part 1 
file = open('1-1/input.txt')

list1 = []
list2 = []
total_distance = 0
for line in file:
    left, right = line.split('   ')

    list1 += [int(left)]
    list2 += [int(right)]

for left, right in zip(sorted(list1), sorted(list2)):
    total_distance += abs(left-right)

print(total_distance)