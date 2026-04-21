'''
Multi - level :-
-------------
This occurs when a class inherits from a child class, creating a grandparents
grandparents-->Parent-->Child in this structure.
1.
class Grandparent:
    def show_Grandparent(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def show_parent(self):
        print("I am parent")
class child(Parent):
    def show_child(self):
        print("I am child")
relation = child()
relation.show_Grandparent()
relation.show_parent()
relation.show_child()
2.    
class modile:
    def show_modile(self):
        print("Update for modile")
class Update(modile):
    def show_Update(self):
        print("Updated apps")
class Updated(Update):
    def show_Updated(self):
        print("App free up space")
app = Updated()
app.show_modile()
app.show_Update()
app.show_Updated()

Hierchical:-
----------
This occurs when multiple child classes inherit from a single parent class,
this process is called Hierchical inheritances

class parent:
    def parent_(self):
        print("I am Parent")
class child_1(parent):
    def child_(self):
        print("I am 1st child")
class child_2(parent):
    def _child(self):
        print("I am child 2")
class child_3(child_1, child_2):
    def child(self):
        print("I am the child")
level = child_3()
level.parent_()
level.child_()
level._child()
level.child()

Hybrid Inheritances:-
-------------------
This the combination of 2 or more types of inheritances such as single,multiple, multi level,or hierchical
all this in single class...
'''
class Grandparent:
    def show_Grandparent(self):
        print("I am Grandparent")
class Parent(Grandparent):
    def show_parent(self):
        print("I am parent")
class child(Parent):
    def show_child(self):
        print("I am child")

class parent:
    def parent_(self):
        print("I am Parent")
class child_1(parent):
    def child_(self):
        print("I am 1st child")
class child_2(parent):
    def _child(self):
        print("I am child 2")
class child_3(child_1, child_2, Grandparent):
    def child(self):
        print("I am from Grandparent class and child_1, child_2")
level = child_3()
level.show_Grandparent()
level.parent_()
level.child_()
level._child()
level.child()
