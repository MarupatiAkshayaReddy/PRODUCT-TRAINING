l=list(map(int,input().split()))
for i in range(len(l)-1):
    min=i
    for j in range(i+1,len(l)):
        if l[j]<l[min]:
            min=j
    l[i],l[min]=l[min],l[i]
for i in range(len(l)):
    print(l[i],end=" ")