'''
constructor(__init__):-
---------------------
-->A constructor is a special method used to initiallize object data
__init__()

class employee:
    def __init__ (self, name, ID):
        self.name = name
        self.ID = ID

    def display(self):
        print(self.name, self.ID)
emp_1 = employee("janu",119)
emp_1.display()

Access Specifiers:-
-----------------
1.Public
2.Protected
3.Private

1.Public:-
  ------
SYNTAX:- name
we can use it anywhere in a program

2.Protected:-
  ---------
SYNTAX:- _name
This is only for internal use

3.Private:-
  -------
SYNTAX:- __name
This one is restricted

self:-
----
This keyword is instances variable and unique for each object
'''
class some:
    def __init__(self):
        self.public = "janu"
        self.protected = "jhanavi"
        self.private = "janujhanavi"

any = some()
print(any.public)
print(any._protected)
print(any.__private)


  
