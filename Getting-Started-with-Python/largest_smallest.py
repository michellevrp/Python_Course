
#fifth exercise
#This code calulcates the largest number.
largest=-1
print('Before', largest)

for the_num in [5 ,84, 63, 92, 5, 71]:
    if the_num>largest:
        largest=the_num
    print(largest,the_num)
print('After',largest)

#sixth exercise
#This code calulcates the smallest number.
smallest=None
print('Before')

for value in [5 ,84, 63, 92, 5, 71]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)        
print('After',smallest)

#seventh exercise
#This code calulcates both the smallest and the largest number.
smallest = None
largest = -1
while True:
    sval = input('Enter a number:')
    if sval == 'done':
        break
    try:
        fval = int(sval)
    except:
        print('Invalid input')
        continue
    if fval > largest:
        largest=fval
        continue
    if smallest is None:
        smallest = fval
    elif fval < smallest:
        smallest = fval
        continue
print('Maximum is', largest)
print('Minimum is', smallest)
