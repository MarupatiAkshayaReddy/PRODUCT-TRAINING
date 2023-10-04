'''n=int(input())
for i in range(1,n+1):
    print(i,end=" ") using iterative'''

#using recursion

def fun(n):
    if n==0:
        return
    else:
        print(n,end=" ")
        fun(n-1)
        print(n,end=" ")
n=int(input())
fun(n)