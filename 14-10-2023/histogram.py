l=[2,3,0,4,6,3,2,1]
for i in range(len(l)):
    print("*"*l[i])#Horizontal histogram
print()
#vertical histogram
for i in range(max(l),0,-1):
    print(f"{i:2d} |",end="")
    for j in l:
        if j>=i:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()

    

    

