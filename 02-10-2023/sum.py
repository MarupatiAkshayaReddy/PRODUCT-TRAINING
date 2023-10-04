def fun(sum,n):
    if n==0:
        return sum
    else:
        sum=sum+n
    return fun(sum,n-1)

n=int(input("enter the value of n:"))
print(fun(0,n))
