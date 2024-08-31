# whether a no is pallindrome or nnot
#121 reverse 121 then it is pallindrome
#657 rverse 756 not pallindrome

n=int(input("enter n digit no\n:"))
num=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
    print("reverse",rev)
    if rev == num:
        print("pallindrome")
    else:
        print("not palindrome")    