'''def check(arr, target, n):
    
    if target == 0:
        return True
    if n == 0:
        return False
        
    if arr[n-1] > target:
        return check(arr, target, n-1)
        
    return check(arr, target-arr[n-1], n-1) or check(arr, target, n-1)
arr = list(map(int,input().split(",")))
target = int(input())
ans = check(arr, target, len(arr))
if ans == True:
    print("solution found")
else:
    print("solution not found")'''

def check(nums,target):
    def backtrack(start,sum):
        if sum==target:
            return True
        if sum>target or start==len(nums):
            return False
        if backtrack(start+1,sum+nums[start]):
            subset.append(nums[start])
            return True
        return backtrack(start+1,sum)
    subset=[]
    if backtrack(0,0):
        return True, subset
    else:
        return False, []
nums=list(map(int,input().split("")))
target_sum=int(input())
bool,subset = check(nums,target_sum)
if bool:
    print("subset with sum",target_sum,"exists:",subset)
else:
    print("No subset with sum",target_sum,"exists:",subset)