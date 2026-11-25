from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog says Bow Bow")


d = Dog()
d.sound()



# from abc import ABC	= Abstract Class కోసం ABC తీసుకుంటున్నాం
# @abstractmethod	    = Abstract Method అని చెబుతున్నాం
# class Animal(ABC)	    = Abstract Class
# def sound(self)	    = Abstract Method
# pass	                = ప్రస్తుతం ఏ పని చేయదు
# class Dog(Animal)	    = Animal నుంచి Inherit చేసుకుంటుంది
# d = Dog()             =   Object Create చేస్తున్నాం
# d.sound()	            = Method Call చేస్తున్నాం

