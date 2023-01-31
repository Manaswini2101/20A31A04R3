Days=84
calls=3000
msgs=100
data=2.0
cday=int(input("enter the day number:"))
if(cday<Days):
    ccalls=int(input("enter the number of calls made:"))
    cmsgs=int(input("enter the number of msgs sent:"))
    cdata=float(input("enter the data amount used:"))
    if(ccalls<calls and cmsgs<msgs and cdata<data):
        d=Days-cday
        c=calls-ccalls
        m=msgs-cmsgs
        g=data-cdata
        print(" number of remaining days:",d)
        print(" number of remaining calls:",c)
        print("number of remaining messages:",m)
        print("amount of data left:",g)
    else:
        print("exceeding the limit.please recharge")
else:
    print("plan validity is expired.recharge for services")
