'''class abc:
    var=10
obj=abc()
print(obj.var)'''
    
'''class abc:
    var=10
    def display(self):
        print("this is in class")
obj=abc()
print(obj.var)
obj.display()'''

'''class abc:
    def __init__(self,value):
        print("this is in class")
        self.value=value
        print("the value is:",value)
obj=abc(1000)'''

'''class abc:
    class_var=0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print("the obj value is :",var)
        print("the class value is:",abc.class_var)
obj1=abc(100)
obj2=abc(101)
obj3=abc(102)'''

'''class abc:
    def __init__(self,var):
        self.var=var
        if var%2==0:
            print("the even number")
        else:    
            print("the odd number")
obj1=abc(21)'''

'''class abc:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            abc.even.append(num)
            print(abc.even)
        else:
           abc.odd.append(num)
           print(abc.odd)
obj=abc(1)
obj=abc(2)
obj=abc(3)
obj=abc(4)
obj=abc(5)
print("even number list:",abc.even)
print("odd number list:",abc.odd)'''

'''class circle:
    pi=3.1459
    def __init__(self,rad):
        self.rad=rad
        circle.area=circle.pi*pow(rad,2)
        circle.circum=2*circle.pi*rad
obj=circle(7.5)        
print("area of the circle is:",circle.area)
print("circumference of the circle is:",circle.circum)'''
        
    