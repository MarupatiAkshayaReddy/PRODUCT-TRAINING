class xyz:
    def __int__(self):
        self.count=0
    
    def toh(n,src,aux,dest):
        if n>0:
            toh(n-1,src,dest,aux)
            self.count+=1
            print(src,dest,n)
            toh(n-1,aux,src,dest)
            self.count+=1
    return self.count
        
n=3
k=xyz()

print(k.toh(n,'a','b','c'))