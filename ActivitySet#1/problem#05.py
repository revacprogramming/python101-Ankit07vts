# Functions


def computepay(h, r):
    if h>40:
       
        rate1=(r*1.5)*(h-40)
        pay=(r*40)+rate1
    else :
        pay=r*h
        
    return pay

hrs = input("Enter Hours:")
h=float(hrs)
rate=input("enter the rate")
r=float(rate)
p = computepay(h,r)
print("Pay", p)