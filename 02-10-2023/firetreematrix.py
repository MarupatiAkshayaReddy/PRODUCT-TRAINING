'''l=[]
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))
    taking input from the user'''


def fun(l,i,j,n):
    
    if l[i][j]==0:
        return 
    
    if l[i][j]==1:
        l[i][j]=0
        
        if i<n-1:
            fun(l,i+1,j,n)
        if i>0:
            fun(l,i-1,j,n)
        if j<n-1:
            fun(l,i,j+1,n)
        if j>0:
            fun(l,i,j-1,n)
        
    return l
    
    
l=[[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,1],[1,1,0,1,0]]
n=len(l)
r=int(input())
c=int(input())
count=0

l=fun(l,r,c,n)
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
print(count)
