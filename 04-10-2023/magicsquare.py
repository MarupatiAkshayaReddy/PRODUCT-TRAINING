n=int(input())
sq=[[0]*n for i in range(n)]
#print(sq)if input=3 [[0, 0, 0], [0, 0, 0], [0, 0, 0]] every where inserted '0'
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
#print(sq) output:-[[9, 3, 22, 16, 15], [2, 21, 20, 14, 8], [25, 19, 13, 7, 1], [18, 12, 6, 5, 24], [11, 10, 4, 23, 17]]
for i in sq:
    #print(i) we will get list one by one 
    print(*i)#if we dont want the []symbols and comma only we want number space use this
print('magic constant:',(n*(n*n+1))//2)