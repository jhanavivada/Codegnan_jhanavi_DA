'''
Polymorphism:-
------------
--> This allows a object different classes to be treated as instances of the same base class,
with methods behaving differently based on obj type.
ex:-
print(len("Python"))
print(len[1,2,3])


Method OverLoading:-
------------------
This defined multiple methods with the same name but different parameters
such as numbers any datatype different order, in the same class

class calculator:
    def add(self, a, b=0, c=0):
        return a+b+c
Cal = calculator()
print(Cal.add(2))
print(Cal.add(19,11))
print(Cal.add(31,30,8)) 

class calculator:
    def mul(self, a, b=1, c=1):
        return a*b*c
Cal = calculator()
print(Cal.mul(2))
print(Cal.mul(1,12))
print(Cal.mul(2,3,4))

class calculator:
    def sub(self, a, b=0, c=0):
        return a-b-c
Cal = calculator()
print(Cal.sub(2))
print(Cal.sub(19,11))
print(Cal.sub(23,13,4))

Method Overriding:-
-----------------
This occurs in the child ,refinding a parent class method wiith the same signature for runtime

class animal:
    def speak(self):
        return "Sound"
class dog(animal):
    def speak(self):
        return "Bark"
Dog = dog()
print(Dog.speak())

class parent:
    def speak(self):
        return "Sound"
class mother(parent):
    def speak(self):
        return "Mother is scolding"
class dad(parent):
    def speak(self):
        return "Dad is scolding"
m = mother()
d = dad()
print(m.speak())
print(d.speak())

Operator Overloading:-
--------------------
This is customizes the operator like +,- for user defind classes by implementing special methods....
ex:-
__add__,__sub__

class addition:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __add__(self, sample):
        return addition(self.a +sample.a, self.b + sample.b, self.c + sample.c)
    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
it = addition(11,19,12)
has = addition(8,39,21)
print(it + has)

Data Abstraction:-
----------------
This hides complex implementation details, exposing only essential features via abstract class or interface.
'''
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
Circle = circle(4)
print(Circle.area())
