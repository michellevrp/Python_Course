#first exercise
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
pay = float(hrs) * float(rate)
print("Pay:", pay)

#second exercise
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Insert numbers")
if h>40:
    p = 40 * r + (((h-40)*1.5)*r)
else:
    p = h * r
p= float(p)
print(p)
