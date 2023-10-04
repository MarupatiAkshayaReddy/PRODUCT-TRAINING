l=list(map(int,input().split()))
flag=False
for i in range(1,len(l)):
    for j in range(len(l)-i):
        if l[j]>l[j+1]:
            flag=True
            l[j],l[j+1]=l[j+1],l[j]
    if flag==False:
        break
    flag=False
for i in range(len(l)):
    print(l[i],end=' ')
            
