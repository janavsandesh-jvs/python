yr=int(input("Enter the number of years you have worked in your company: "))
sal=int(input("Enter your salary: "))
if yr>10:
  bns=sal*0.10
elif yr>=5 and yr<=10:
  bns=sal*0.05
else:
  bns=sal*0.02

print ("salary: ", sal) 
print ("Bonus: ", bns)
print ("Salary with bonus: ", sal+bns)

