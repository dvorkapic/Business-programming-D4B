num = float(input('please enter the order total: '))

if num >=100:
    print('Final amount is ', num-(num*0.1))
else:
    print('Final amount is ', num)