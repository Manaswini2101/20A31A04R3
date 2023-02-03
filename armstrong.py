sum=0
n=(input("enter value:"))
order=len(str(n))
a=n
while(n!=0):
    r=int(n)%10
    sum+=r**order
    n=int(n)//10
if sum==a:
    print("Armstrong")
else:
    print("not Armstrong")