#single line inheritance
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

# Creating an object of the Child class
child = Child("Alice", 10)
print(child.name)  # Output: Alice
print(child.age)   # Output: 10

#multiple inheritance 
class Parent1:    
    def method1(self):
        print("Method from Parent1")   
        
class Parent2:
    def method2(self):
        print("Method from Parent2")   

class Child(Parent1, Parent2):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

# Creating an object of the Child class
child = Child("Bob", 15)
child.method1()  # Output: Method from Parent1
child.method2()  # Output: Method from Parent2

#MULTI-LEVEL INHERITANCE
class Grandparent:
    def method1(self):
        print("Method from Grandparent")
        
class Parent(Grandparent):
    def method2(self):
        print("Method from Parent")

class Child(Parent):
    def method3(self):
        print("Method from Child") 

# Creating an object of the Child class
child = Child()         
child.method1()  # Output: Method from Grandparent
child.method2()  # Output: Method from Parent
child.method3()  # Output: Method from Child   

#Hierarchical Inheritance
class Parent:
    def method1(self):
        print("Method from Parent")

class Child1(Parent):
    def method2(self):
        print("Method from Child1")

class Child2(Parent):
    def method3(self):
        print("Method from Child2")

# Creating objects of the child classes
child1 = Child1()
child2 = Child2()

child1.method1()  # Output: Method from Parent
child1.method2()  # Output: Method from Child1

child2.method1()  # Output: Method from Parent
child2.method3()  # Output: Method from Child2 


#hybrid Inheritance
class Parent:
    def method1(self):
        print("Method from Parent")
class Child1(Parent):
    def method2(self):
        print("Method from Child1") 
class Child2(Parent):
    def method3(self):
        print("Method from Child2")
class Grandchild(Child1, Child2):
    def method4(self):
        print("Method from Grandchild") 
class Grandchild2(Child1, Child2):
    def method5(self):
        print("Method from Grandchild2")    
class Grandchild3(Child1, Child2):
    def method6(self):
        print("Method from Grandchild3")    

class Grandchild4(Child1, Child2):
    def method7(self):
        print("Method from Grandchild4")
class Grandchild5(Child1, Child2):
    def method8(self):
        print("Method from Grandchild5")    
Creating objects of the grandchild classes
grandchild1 = Grandchild()  

