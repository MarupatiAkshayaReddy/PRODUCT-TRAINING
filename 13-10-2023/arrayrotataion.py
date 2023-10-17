#array rotation-using temp variable
arr=list(map(int,input().split(",")))
k=int(input())
n=len(arr)
'''left rotation
for i in range(k):
    temp=arr[0]
    for j in range(1,n):
        arr[j-1]=arr[j]
    arr[n-1]=temp
print(arr)'''

#right rotation-right element placing in left position
'''for i in range(k):
    temp=arr[-1]
    for j in range(n-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=temp
print(arr)'''

#array rotation-using temp array
'''res=[]
for i in range(k,n):
    res.append(arr[i])
for i in range(k):
    res.append(arr[i])
print(res)'''

#using slice operator
'''res1=[]
res2=[]
res1=arr[:k] #slice operator
res2=arr[k:]
#res2.append(res1)#[5, 6, [2, 3, 4]]
for i in range(len(res1)):
    res2.append(res1[i])
print(res2)'''


#using slice operator in the same array not using another array
if k>=len(arr):
    k=k%len(arr)
if len(arr)==0 or k==0:
    print(arr) 
a=len(arr)-k
arr[:]=arr[a:]+arr[:a]
print(arr)


#using pop and insert function
#insert()-it will not replace anything by default it will the shift the elements in the array
#in 1st iteration the array-2,3,4,5,6 will convert to 6,2,3,4,5(just shifting)-5,6,2,3,4----4,5,6,2,3
'''for i in range(k):
    arr.insert(0,arr.pop())
    print(arr)
print(arr)'''




