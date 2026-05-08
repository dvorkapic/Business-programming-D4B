list = [10,20,5,40]
total = 0
for item in list:
    total += item

if total > 50:    
    print(total-(total*0.1))    
else:
    print(total)