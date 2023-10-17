#finding sum of array elements using divide and conquer approach
def sum(l,si,ei):
    if si==ei:
        return l[si]
    if si>ei:
        return -1
    mid=(si+ei)//2
    return max(sum(l,si,mid),sum(l,mid+1,ei))

l=list(map(int,input().split()))
print(sum(l,0,len(l)-1))
