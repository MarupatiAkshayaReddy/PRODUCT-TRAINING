wt=list(map(int,input().split()))
p=list(map(int,input().split()))
w=int(input())

l=list(zip(wt,p))
#print(list(l))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
print(list(l))
maxpr=0
for weight,profit in l:
    if weight<=w:
        maxpr+=profit
        w-=weight
    else:
        maxpr+=w*(profit/weight)
        break
print(maxpr)

       
