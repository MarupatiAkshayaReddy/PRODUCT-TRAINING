def sqrt(n,si,ei,ceil):
    if n==1:
        return 1
    elif n<0:
        return -1
    else:
        if si<=ei:
            mid=(si+ei)//2
            sq=mid*mid
            if sq==n:
                return mid
            elif sq<n:
                return sqrt(n,mid+1,ei,ceil)
            else:
                ceil=mid
                return sqrt(n,si,mid-1,ceil)
        return ceil

n=int(input())
print(sqrt(n,0,n//2,float('inf')))
