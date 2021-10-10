
#fourth exercise
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
	h = float(hrs)
	r = float(rate)
except:
    print("Insert numbers")
 def computepay(h, r):
    if h>40:
        p = float(40 * r + (((h-40)*1.5)*r))
        return p

pay = computepay(h,r)
print("Pay", pay)

