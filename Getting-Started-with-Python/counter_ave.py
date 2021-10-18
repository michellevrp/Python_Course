#eighth
#This code counts the elements.
counter = 0
print('Before', counter)
for thing in [54, 9, 62, 5, 35, 84]:
    counter = counter + 1
    print(counter, thing)
print('After', counter)

#nineth
#This code calculates the sum of the numbers.
counter = 0
print('Before', counter)
for thing in  [54, 9, 62, 5, 35, 84]:
    counter = counter + thing
    print(counter, thing)
print('After', counter)    

#tenth exercise
#This code counts the elements, calculates the sum and the average of the numbers.
count = 0
sum = 0
print('Before', count, sum)
for value in  [54, 9, 62, 5, 35, 84]:
    count = count + 1
    sum = sum + value 
    print(count, sum, value)
print('After', count, sum, sum/count)    

#eleventh
#This code counts the elements, calculates the sum and the average of the numbers with the while function.
num = 0
tot = 0.0
while True:
    sval = input('Enter a number:')
    if sval == 'done': 
        break 
    try:
        fval = float(sval)
    except:
        print('Invalid input')
    print(fval)
    num = num = 1
    tot = tot +fval

print('ALL DONE')
print(tot,num,tot/num)
