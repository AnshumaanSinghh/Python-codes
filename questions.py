n=int(input("enter no:"))

for i  in  range(1,n+1):
    #printing spaces 
    print(" " * (n-i),end="")
    #printing digits

    for j in range(1,2*i):
        print(j,end="")
    print("")    




