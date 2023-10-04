class Siva:
    def gold(warangal):
        print("price 5L")
    def car(warangal):
        print("price 3L")
class Baby1(Siva):
    def magic(xyz):
        n=int(input("read a prime number:"))
        temp=n;
        rev=0
        c=0
        while(n>0):
            r=n%10
            rev=rev*10+r
            n=n//10
        for i in range(1,temp+1):
            if(temp%i==0):
                c=c+1
        if(c==2):
            print("magic number")
        else:
            print("non magic number")
        
class Baby2(Siva):
    def neon(xyz):
        print("neon numbers are:")
        for i in range(0,100+1):
            s=i*i
            temp=s
            sum=0
            if(i==0):
                print(i,end=" ")
            else:
                while(s>0):
                    r=s%10
                    sum=sum+r
                    s=s//10
                if(sum==i):
                    print(i,end=" ")
        print('\n')
                    
b1=Baby1()
b1.magic()
b1.gold()
b1.car()

b2=Baby2()
b2.neon()
b2.gold()
b2.car()

