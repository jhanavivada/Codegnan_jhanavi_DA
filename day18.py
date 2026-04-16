'''Introduction to OOP's
Classes
Objects
Attributes
Methods

OOP's:-
------
--> Object-Oriented Language(OOP) is a style of programing whrere we model
real_world thing as object that contain both data and functions()
--> reusable of the code
--> and also scalable 
class
----
class is a blue-print or template that defines what kind of data and behavior certain type of object have

Objects:-
-------
-->this is Instance of class or an object is a real instances from a class.
It is tha actual thing that exists in memory while the program runs
ex:-
class car:
    Pass
car1 = car()  #objects
car2 = car()

Attributes:-
----------
--> this are the variables that store data related to a class or object

class Dog:
    def __init__(self, breed, color, size):
        self.breed = breed
        self.color = color
        self.size = size
dog_1 = Dog("german", "black", "medium")
dog_2 = Dog("bulldog", "white", "small")
print(dog_1.breed)

for animals:-

class Animal:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size
animal_1 = Animal("lion", "brown", "medium")
animal_2 = Animal("cat", "white", "small")
print(animal_1.name)

for food items:-

class Food_items:
    def __init__(self, name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price
items_1 = Food_items("rice","high","100")
items_2 = Food_items("dal","medium","50")
items_3 = Food_items("curry","small","80")
print(items_2.price)

for vegetables:-

class vegetables:
    def __init__(self, name,quantity):
        self.name = name
        self.quantity = quantity
Veg_1 = vegetables("potato","1kg")
Veg_2 = vegetables("carrot","2kg")
print(Veg_2.name)
'''
class car:
    wheels = 4

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 20

    def drive(self, miles):
        self.mileage += miles
        return f"Drove {miles} miles. Total: {self.mileage}"

    def info(self):
        return f"{self.make} {self.model} {self.year}"

car_1 = car(make="Ford", model="Mustang", year="2008")
car_2 = car(make="Toyota", model="Camry", year="2023")

print(car_1.info())
print(car_2.info())
print(car_2.drive(10))
