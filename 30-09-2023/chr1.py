a=input()
b=int(input())

'''if(ord(a)>96):
    if(ord(a)+b>122):
        y=b-26
        print(chr((ord(a)+y)+65+y))
    else:
        print(chr(ord(a)+b))'''
if(ord(a)+b>122):
    print(chr((ord(a)+b)-26))
else:
    print(chr(ord(a)+b))
    
    


    


