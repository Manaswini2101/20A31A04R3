'''for i in range(1,21,2):
    print(i,end=" ")'''

'''n=10
s=0
avg=0
for i in range(1,n+1):
    s=s+i
    avg=s/n
print("sum of 10 natural numbers is",s)
print("average of 10 natural numbers is",avg)'''

'''n=int(input("enter a value:"))
print("multiplication table of ",n)
for i in range(1,11):
    print(n,"X", i,"=",n*i)'''

'''n=int(input("enter a value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial is :",fact)'''

'''n=int(input("enter a value:"))
sum=0
for i in range(1,n+1):
    sum=sum+1/i
print(sum)'''

'''n=int(input("enter a value:"))
sum=0
for i in range(1,n+1):
    sum=sum+(i/(i+1))
print(sum)'''

'''n=int(input("enter a value:"))
E=0
O=0
i=0
while(n!=0):
    rem=n%10
    if(rem%2==0):
        E=rem+E
    else:
        O=rem+O
    n=n//10    
print("difference of terms is:",abs(O-E))'''

'''n=(str(input("enter a value:")))
print(int(n,17))'''

'''n=[1,2,3,4,5,6,7]  #output:1 2 3 5 6 7
for i in n:
    if i==4:
        continue
    print(i,end=" ")'''

'''n=[1,2,3,4,5,6,7]    #output: 1 2 3
for i in n:
    if i==4:
        break
    print(i,end=" ")'''

'''for letter in 'manaswini':     
    print("pass:",letter)'''

term=int(input("enter a term:"))
if term%2==0:
    term=term//2
    print(3**(term-1))
else:
    term=term//2+1
    print(2**(term-1))