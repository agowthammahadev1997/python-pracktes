class parent:
        def fun1(self):
            print("This is parent class")
class child(parent):
        # def fun2(self):
            # print("This is child class")
obj = child()
obj.fun1()
obj.fun2()
