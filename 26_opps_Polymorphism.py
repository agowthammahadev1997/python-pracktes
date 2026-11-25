# # Polymorphism
# class Dog:

#     def sound(self):
#         print("Dog barks")


# class Cat:

#     def sound(self):
#         print("Cat meows")


# class Cow:

#     def sound(self):
#         print("Cow moos")


# dog = Dog()
# cat = Cat()
# cow = Cow()

# dog.sound()
# cat.sound()
# cow.sound()

#Method Overriding
"""Parent Classలో ఒక Method ఉంటుంది.
Child Classలో అదే Methodను మళ్లీ రాసి కొత్త Behavior ఇవ్వడాన్ని Method Overriding అంటారు."""

class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()



#Method Overloading
class Calculator:

    def add(self, a, b=0, c=0):
        print(a + b + c)


obj = Calculator()

obj.add(10)
obj.add(10, 20)
obj.add(10, 20, 30)