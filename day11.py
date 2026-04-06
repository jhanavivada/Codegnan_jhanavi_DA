'''
functions:-
--------
--> this a block of code which is reuseble.
--> this are 2 types
   1.Bulit-in or In-built
   2.User defind

1.Bulit-in or In-built
----------------------
--> they comes with program and those are already defind...
ex:- print(), sum(), map()....

2.User defind
-------------
--> this is created by person who is developing or using for development

note
----
--> it starts with the def keyword followed by func name (calling function)
--> And it has calling func.... (calling line)
syn:-
----
def func_name():
    __________
    __________
    __________
    __________
func_name()
in the () are knows as parameters
and the func_name() are knows as argements

def even_odd(a):
    if a%2 == 0:
       print(f"{a} is even") 
    else:
       print(f" {a} is odd")
even_odd(a=2)

prime_num = 11
count = 0
def prime_check(Num,k):
    for j in range(1,Num+1):
        if Num % j == 0:
           k +=1
    if k == 2:
        print("prime")
    else:
        print("not")
prime_check(prime_num,count)

differeent b/w (==), (is) operator:-

a = [1,2]
b = [1,2]
print(a == b)
'''
a = [1,2]
b = [1,2]
c = b
print(id(c),id(b))
print(c is b)    






