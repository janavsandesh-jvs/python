vph=int(input("Enter the number of hours you parked your vehicle: "))
if vph==1:
  pc=20
elif vph>=2 and vph<=4:
  pc=vph*10
else:
  pc=vph*5
print ("parking charge: ", pc) 
