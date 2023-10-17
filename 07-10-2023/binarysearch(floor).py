def bs(arr,key,si,ei,floor):
    if si<=ei:
        mid=(si+ei)//2
        if arr[mid]==key:
            return arr[mid]
        elif arr[mid]<key:
            return bs(arr,key,mid+1,ei,arr[mid])
        else:
            return bs(arr,key,si,mid-1,floor)
    return floor



arr=list(map(int,input().split()))
key=int(input())
n=len(arr)-1
print(bs(arr,key,0,n,-1))


    
