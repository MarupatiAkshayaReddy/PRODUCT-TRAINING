'''l=list(map(int,input().split()))
n=int(input())
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==n:
                print("found")'''
l=list(map(int,input().split()))
n=len(l)
l.sort()
target=int(input())
for i in range(n):
    left=i+1
    right=n-1
    while left<right:
        sum=i+l[left]+l[right]
        if sum==target:
            print("found")
            break
        elif sum<target:
            left+=1
        else:
            right-=1
               
