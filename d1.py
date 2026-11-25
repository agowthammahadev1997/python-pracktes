# class Car:
#     def __init__(self, color, max_speed, acceleration, tyre_friction):
#         self.color=color
#         self.max_speed=max_speed
#         self.acceleration=acceleration
#         self.tyre_friction=tyre_friction


# # You need not change any code below.
# # Do not call this function anywhere. It will automatically be called internally during tests.
# def default_test():
#     print(car.color)
#     print(car.max_speed)
#     print(car.acceleration)
#     print(car.tyre_friction)

# car1 = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)
# car2 = Car(color="Blue", max_speed=300, acceleration=15, tyre_friction=5)
# print(car1.color, car1.max_speed)  
# print(car2.color, car2.max_speed)

#singe inheritance
class Parent:
    def __init__(vamsi, name, age):
        vamsi.name = name
        vamsi.age = age

    def method1(vamsi):
        print("Name:", vamsi.name)
        print("Age:", vamsi.age)


class Child(Parent):
    def method2(vamsi):
        print("Method from Child")


a = Child("Vamsi", 21)

a.method1()
a.method2()