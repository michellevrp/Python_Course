#fourth exercise
#This code asks the user for hours and rate for hour, calculate total pay by computepay function, and print it. 
#If more than 40 hours, the rate is 1.5 the initial rate.
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

