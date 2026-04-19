'''
Generators
----------
this is a special type of functions that return an ITERATOR which one at a time

yield:-
--> It will take a pause and again resume,this is not a normal keyword cann't be used in the normal functions
--> this is used to produce a value and pause execution.

next():-
-----
--> this is used to get next value from a generators
--> when the value is finished,it will stop the iterator

def generator():
    yield 11
    yield 24
    yield 19
    yield 11
are = generator()
print(next(are))
print(next(are))
print(next(are))
print(next(are))

def square(n):
    for i in range(n):
        yield i * i
for val in square(7):
    print(val)
'''
def add(n):
    for i in range(n):
        yield i + 10
for val in add(5):
    print(val)
    








    
