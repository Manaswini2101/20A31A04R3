'''def total(a,b):
    result=a+b
    print("function result is :",result)
def sub(a,b):
    result2=a-b
    print("function result is :",result2)
def mul(a,b):
    result3=a*b
    print("function result is :",result3)
def div(a,b):
    result4=a//b
    print("function result is :",result4)
a=int(input("enter a value:"))
b=int(input("enter b value:"))
total(a,b)
sub(a,b)
mul(a,b)
div(a,b)'''
 
'''def mn(b):
    print("give manu a sum of",b)
mn(5*10)'''

'''b="manu"
def show():
    global b1
    b1="white girl"
    print("in function b cis",b1)
show()
print("outside func",b)
print(" b is ",b)'''

'''def outf():
    var=10
    def innf():
        var=20
        print("inner var",var)
    innf()
     print("outer var",var)
outf()'''

'''def cubic(b):
    return(b*b*b)
num=10
result=cubic(num)
print("output of evaluation is:",result)'''

'''def sumof(a,b,c,d,e,f):
    return(a+b+c+d+e+f)
a,b,c,d,e,f=0,2,4,6,8,10
result=sumof(a,b,c,d,e,f)
print("output is:",result)'''

def fibanocci(b):
    if b<2:
        return 1
    else:
        return(fibanocci(b-1)+fibanocci(b-2))
b=int(input())
for i in range(b):
    print("fibanocci(",i,")",fibanocci(i))
    