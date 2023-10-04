def toh(n,src,aux,dest):
    if n>0:
        toh(n-1,src,dest,aux)#source to auxillary with the help of destination
        print(src,dest,n)
        toh(n-1,aux,src,dest)#auxillary to destination with the help of source(the stick which we are using as a help we
                            #will write in middle of the function call)
n=3
toh(n,'a','b','c')

'''def toh(n,src,aux,dest):
    if n==1:
        return 1
    else:
        return toh(n-1,src,dest,aux)+1+toh(n-1,aux,src,dest)
n=int(input("enter no:of discs:"))
print(toh(n,'a','b','c'))'''