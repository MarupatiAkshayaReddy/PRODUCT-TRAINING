def twopo(l,target):
    left=0
    right=n-1
    while left<right:
        sum=l[left]+l[right]
        if sum==target:
            return left,right
            break
        elif sum<target:
            left+=1
        else:
            right-=1
    

l=list(map(int,input().split()))
n=len(l)
target=int(input())
ans=twopo(l,target)
print(ans[0],",",ans[1])
    