class GrandFather():
    def __init__(self):
        self._a=10 
        self.__b=20 
    def _fun1(self):
        print("This is our House") 
    def __fun2(self):
        print("This is my Farm House") 
class Father(GrandFather):
    def fun3(self):
        print("I have 10cr") 
ob=GrandFather() 
ob._GrandFather__fun2()   # Data Mangling 

