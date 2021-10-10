#first exercise

# hrs = input("Enter Hours:")
# rate = input("Enter Rate:")
# pay = float(hrs) * float(rate)
# print("Pay:", pay)

#   #second exercise
# hrs = input("Enter Hours:")
# rate = input("Enter Rate:")
# try:
#     h = float(hrs)
#     r = float(rate)
# except:
#     print("Insert numbers")
# if h>40:
#  	p = 40 * r + (((h-40)*1.5)*r)
# else:
#     p = h * r
# p= float(p)
# print(p)

#  #third exercise
# score = input("Enter Score: ")
# try:
#     sc = float(score)
# except:
#     print("Insert numeric input")
# if sc >= 0.9:
#     print("A")
# elif sc >= 0.8:
#     print("B")
# elif sc >= 0.7:
#     print("C")
# elif sc >= 0.6:
#     print("D")
# elif sc<0.6:
#     print("F")

# #fourth exercise
# hrs = input("Enter Hours:")
# rate = input("Enter Rate:")
# try:
# 	h = float(hrs)
# 	r = float(rate)
# except:
#     print("Insert numbers")

# def computepay(h, r):
#     if h>40:
#         p = float(40 * r + (((h-40)*1.5)*r))
#         return p

# pay = computepay(h,r)
# print("Pay", pay)

#fifth exercise
largest=-1
print('Before', largest)

for the_num in [5 ,84, 63, 92, 5, 71]:
    if the_num>largest:
        largest=the_num
    print(largest,the_num)
print('After',largest)
