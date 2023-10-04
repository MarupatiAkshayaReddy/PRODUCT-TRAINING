'''def cse():
    print("hi")
def ece():
    print("hello")
ece()
cse()
cse()
ece()'''

def cse():
    print("hi")
def ece(x,y):
    print("hello",x+y)
ece(5,6)
cse()
