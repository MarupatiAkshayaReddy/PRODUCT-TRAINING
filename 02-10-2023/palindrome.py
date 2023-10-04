'''a=input()
i=0
j=len(a)-1

while(i<j):
    if(a[i]!=a[j]):
        print("not palindrome")
        break
    i+=1
    j-=1
else:
    print("palindrome")
    iterative'''

#recursive      
def fun(a,i,j):
    if i>j:
        return True
    if a[i]!=a[j]:
        return False
    return fun(a,i+1,j-1)
        
        
a=input()
print(fun(a,0,len(a)-1))

        
    
    