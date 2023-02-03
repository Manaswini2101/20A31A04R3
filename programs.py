'''term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(1*(term-1))
else:
    term=term//2+1
    print(2*(term-1))'''

n=int(input("enter a value:"))
max=count=flag=0
x=input()
arr=list(x)
for i in range(0,n):
    if(arr[i]=='1'):
        count+=1
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)        
