class cse:
    def fun1(self):
        print("fun1-father")
class two:
    def fun2(self):
        print("university")
class three(cse):
    def fun3(self):
        print("hello")
        super().fun1()
obj=three()
obj.fun3()
