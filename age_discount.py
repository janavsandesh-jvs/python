a=int(input("Enter your age: "))
tp=int(input("Enter your ticket price: "))
if a<12:
  disc=0.50*tp
elif a>=60 :
  disc=0.40*tp
else:
  disc=0
print ("Ticket price with discount: ", tp+disc)  
