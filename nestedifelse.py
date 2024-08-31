#find no is divisible of 5 and 3 not by 15 of greatest
num=int(input("enter the number"))

if num%15==0:
    print("no is divisible by 15")
else:
    if num%3 ==0 or num%5==0:
        print("Number is not divisible by 15 but divible by 3 and 5:")
    else:
        print('no is neither divisible by 3 or 5')
