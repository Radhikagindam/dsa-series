class Father():
    def fun1(self):
        print("i can do job") 
class Mother():
    def fun2(self):
        print("i can cook") 
class Son(Father,Mother):
    def fun3(self):
        print("i can play") 
ob=Son()
ob.fun1()

