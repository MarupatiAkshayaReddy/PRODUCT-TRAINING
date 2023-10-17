def thpo(l,target):
    for i in range(n):
        left=i+1
        right=n-1
        while left<right:
            sum=l[i]+l[left]+l[right]
            if sum==target:
                return i,left,right
                break
            elif sum<target:
                left+=1
            else:
                right-=1
               
l=list(map(int,input().split()))
n=len(l)
l.sort()
target=int(input())
ans=thpo(l,target)
print(ans[0],",",ans[1],",",ans[2])

 