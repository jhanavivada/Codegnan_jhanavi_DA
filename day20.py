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
'''
class person:
    def name(self):
        print("name: janu")
class address:
    def addr(self):
        print("address: AP")
class contact:
    def mobile(self):
        print("mobile: 8967452301")
class dob:
    def date(self):
        print("dob: 11-08-2003")
class adhar(person,address,contact,dob):
    def adhar_no(self):
        print("adhar number: 1119 0811 1903")
date=adhar()
data.name()
data.addr()
data.mobile()
data.date()
data.adhar_no()



