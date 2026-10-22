n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
n3=int(input("Enter a number: "))
if n1>n2 and n1>n3:
  print (f"{n1} is the greatest")
elif n2>n1 and n2>n3:
  print (f"{n2} is greatest")
elif n3>n1 and n3>n2:
  print (f"{n3} is the greatest")
else:
  print ("all are equal")
