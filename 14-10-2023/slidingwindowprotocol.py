l=list(map(int,input().split(",")))
target=int(input())
currsum=l[0]
i=0
j=0
while j<len(l)-1:
    if currsum==target:
        print(i,"to",j,"indexes",currsum)
        break
    elif currsum>target:
        currsum-=l[i]
        i+=1
    else:
        j+=1
        currsum+=l[j]
            
            
            
        
        