'''Encapsulation:-
   -------------
-->The principle of bunding data(Attributes) and methods that operate on that data into a single unit,
which is a class

class BankAC:
    def __init__(self, balance):
        self.__balance = balance
    def deposite(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
Acc = BankAC(11000)
Acc.deposite(9000)
print(Acc.get_balance())

Inheritance:-
-----------
--> This allows child class(Sub class) to acquire the attributes and methods of a parent class(Base class)
this is called Inheritance
Types:
1.Single Inheritance :- Accesing only single inheritance,Using single method of the class from base class
2.Multiple Inheritance:- A child class Inheritance from more than one parent class 

Super():-
------
--> This is used to call methods of the parent class from the child class

Ex Single Inheritance:-

class parent:
    def display(self):
        print("This is OOPS Base class method")
class child(parent):
    def display(self):
        super().display()
        print("This is OOPS Sub class method")
methods = child()
methods.display()

Ex Multiple Inheritance:-
'''
class Father:
    def skill_1(self):
        print("Father: Focused")
class Mother:
    def skill_2(self):
        print("Mother: Inteligent")
class Child(Father, Mother):
    def All_skills(self):
        print("Child: Hard Working")
relation = Child()
relation.skill_1()
relation.skill_2()
relation.All_skills()




