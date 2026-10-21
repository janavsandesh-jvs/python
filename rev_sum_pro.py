num=int(input("Enter a number: "))
rev=0
sum=0
pro=1
for i in range (len(str(num))):
  digit=num%10
  rev=rev*10+digit
  sum+=digit
  pro*=digit
  num=num//10
print ("Reversed digits: ", rev)  
print ("Sum of digits: ", sum)
print ("Product of digits: ", pro)
