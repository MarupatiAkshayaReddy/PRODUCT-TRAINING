'''n=int(input())
si=0
li=n//2
floor=-1
while si<=li:
    mid=(si+li)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        si=mid+1
    else:
        li=mid-1
print(floor)

def sqrt(n,si,ei,floor):
    if n==1 :
        return 1
    elif n<0:
        return 0
    else:
        if si<=ei:
            mid=(si+ei)//2
            sq=mid*mid
            if sq==n:
                return mid
            elif sq<n:
                floor=mid
                return sqrt(n,mid+1,ei,floor)
            else:
                return sqrt(n,si,mid-1,floor)
        return floor


n=int(input())
print(sqrt(n,0,n//2,-1))'''

def sqrt_bs(number,epsilon=1e-8):
    if number<0:
        raise ValueError("cannot compute")
    if number<1:
        left,right=number,1
    else:
        left,right=0,number
    while abs(left-right)>epsilon:
        
        mid=(left+right)/2
        mid_square=mid*mid
        
        if mid_square<number:
            left=mid
        else:
            right=mid
        
        return (left+right)/2
num=int(input())
result=sqrt_bs(num)
print("square root of the number is:",result)
            
            
        


    

