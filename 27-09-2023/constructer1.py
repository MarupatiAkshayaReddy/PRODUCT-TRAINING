'''constructer overloading and constructer overriding comes under polymorphism concept'''

class Siva:
    def __init__(mango):
        print("default constructer")
    def __init__(mango1,mango2):
        print("2 parametrized constructer",mango2)
        super().__init__()
    def __bank__(india):
        print("test 1")
    def jeno(manglore):
        print("test 2")
    def jeff(banglore):
        print("test 3")
s=Siva(125)
s.jeno()
s.jeff()
s.__bank__()

