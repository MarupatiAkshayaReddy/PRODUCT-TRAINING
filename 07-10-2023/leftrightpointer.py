#two pointer algorithm
arr=list(map(int,input().split()))
left=0
right=len(arr)-1
target=int(input())

while left<right:
    
    sum=arr[left]+arr[right]
    if sum==target:
        print("found")
        break
    elif sum<target:
        left+=1
    else:
        right-=1
    