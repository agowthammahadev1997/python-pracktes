class Student:
    #__init__ method to initialize the attributes of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def study(self):
        print(self.name, "is studying")

# Creating objects
student1 = Student("Gowtham", 21)
student2 = Student("Ravi", 22)


#printing the attributes of the objects
print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)
# Calling the study method for each object              
student1.study()
student2.study()


class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction


# You need not change any code below.
# Do not call this function anywhere. It will automatically be called internally during tests.
def default_test():
    print(car.color)
    print(car.max_speed)
    print(car.acceleration)
    print(car.tyre_friction)

car1 = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
car2 = Car(color="Blue", max_speed=300, acceleration=15, tyre_friction=5)
print(car1)  
print(car2) 
