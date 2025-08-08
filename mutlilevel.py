class GrandFather():
    def fun1(self):
        print("i can farm") 
class Father(GrandFather):
    def fun2(self):
        print("i can do job") 
class Son(Father):
    def fun3(self):
        print("i can play") 
ob=Son() 
ob.fun1() 
