list = []
count = 0
item = str(input('Input item name: '))

while item !='done':
    item = str(input('Input item name: '))
    list.append(item)
    count += 1

print('You have', count, 'items')
print(list)