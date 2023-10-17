def bs(arr,key,si,ei):
    if si<=ei:
        mid=(si+ei)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return bs(arr,key,mid+1,ei)
        else:
            return bs(arr,key,si,mid-1)
    return -1



arr=list(map(int,input().split()))
key=int(input())
n=len(arr)-1
print(bs(arr,key,0,n))

    
