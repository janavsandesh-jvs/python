rs=int(input("Enter the number of rupees you used: "))
if rs>2000:
  disc=rs*0.20
elif rs>=1000 and rs<=2000:
  disc=rs*0.10
else:
  disc=0
print (f"discount:  {disc:.2f}")
print ("rupees after discount: ", rs-disc)
