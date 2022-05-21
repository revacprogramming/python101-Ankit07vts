# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter the rate")
r=float(rate)

if h>40 :
  rate1=(r*1.5)*(h-40)
  pay=((h-5)*r)+rate1
  print(pay)
else :
  print(h*r)
    
