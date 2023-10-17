'''n=int(input())
l=[True]*(n+1)

for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        for j in range(i*i,n+1,i):
            l[i]=False
print(l)'''

def sieve(n):
    prime=[True]*(n+1)
    p=2
    while(p*p<=n):
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p+=1
    for p in range(2,n+1):
        if prime[p]:
            print(p,end=" ")

            
n=int(input())
sieve(n)
    
        
    
    