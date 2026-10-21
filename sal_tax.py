sal=int(input("Enter your salary: "))
if sal<=300000:
  tax=0
elif sal>300000 and sal<=600000:
  tax=sal*0.05
elif sal>600000 and sal<=1000000:
  tax=sal*0.10
else:
  tax=sal*0.20
print ("net salary: ", sal-tax)  
