def bs(arr,key,si,ei,ceil):
    if si<=ei:
        mid=(si+ei)//2
        if arr[mid]==key:
            return arr[mid]
        elif arr[mid]<key:
            return bs(arr,key,mid+1,ei,ceil)
        else:
            return bs(arr,key,si,mid-1,arr[mid])
    return ceil



arr=list(map(int,input().split()))
key=int(input())
n=len(arr)-1
ceil=float('inf')
print(bs(arr,key,0,n,ceil))


    


