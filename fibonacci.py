nterm=int(input("how many terms?:"))
n1,n2 = 0,1
count=0
if nterm<=0:
    print("please enter positive number")
elif nterm==1:
    print("fibonacci series is",nterm,":")
    print(n1)
elif nterm ==2:
    print("fibonacci series upto",nterm,":")  
    print(n1)
    print(n2)
else:
    print("fibonacci sequence:")
    print(n1)
    print(n2)
    for i in range(3,nterm+1):
        nth =n1+n2
        print=(nth)
        n1=n2
        n2=nth


