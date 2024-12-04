# Dec 1 2024 - part 2
file = open('1-2/input.txt')

list1 = []
list2 = []
similarity_score = 0
for line in file:
    left, right = line.split('   ')

    list1 += [int(left)]
    list2 += [int(right)]

list1 = sorted(list1)
list2 = sorted(list2)

i = 0 
j = 0
while i < len(list1) and j < len(list2):
    num1 = list1[i]
    num2 = list2[j]
    if num1 == num2:
        similarity_score += num2
        j += 1
        continue
    elif num1 < num2:
        i += 1
    else:
        j += 1

print(similarity_score)