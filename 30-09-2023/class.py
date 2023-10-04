'''class cse:
    x=10
    static variable can be accessed without object'''
    '''def __init__(self):
        self.y=30
        '''non-static variable'''
        
        
    def qwer(self):
        print("hi")

a=cse()
a.qwer()
print(cse.x,a.y)

cse.qwer(a)
to call method
1.class name.method name(object)
2.using object.method name()'''

class cse:
    x=10
    def __init__(self,k):
        self.y=k
        
        
    def qwer(self):
        print("hi",self.y)

a=cse(80)
b=cse(12)
b.qwer()
