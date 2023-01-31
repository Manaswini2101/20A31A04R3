email="balaji@gmail.com"
pswd=123456
otp=5678
cemail=input("enter the email:")                                  
cpswd=int(input("enter the password:"))
if(email==cemail and pswd==cpswd):
    print("login successful")
    cotp=print(int(input("enter the otp:")))
    if(cotp==otp):
        print("amazon order placed successful")
    else:
        print("invalid otp and order not placed")
elif(email!=cemail and pswd==cpswd):
    print("login failed due to wrong email")
elif(email==cemail and pswd!=cpswd):
    print("login failed due to wrong password")
elif(email!=cemail and pswd!=cpswd):
    print("login failed due to wrong email and password")
else:
    print("login failed")
