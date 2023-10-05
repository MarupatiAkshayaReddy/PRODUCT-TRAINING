#time complexity:=o(n^2)
l=list(map(int,input().split()))
count=0
print("inersion pairs are:")
#i should always less than j
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            print(l[i],l[j])
            count+=1
print("inversion count:",count)