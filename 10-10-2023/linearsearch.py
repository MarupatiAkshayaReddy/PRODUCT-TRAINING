l=list(map(int,input().split()))
target=int(input())
flag=False
for i in range(len(l)):
    if l[i]==target:
        index=i
        flag=True
        break
if flag==True:
    print(index)
else:
    print("-1")