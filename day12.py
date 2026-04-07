'''
Way to pass arguments in calling

Required arguments :-
------------------
 --> is should match same number varibales in calling with def
 
a_num = 19
b_num = 11
def mul(a_num, b_num):
    print(a_num * b_num)
mul(a_num,b_num)    

name = "janu"
def add(name):
    print(name)
add(name = "jhanavi")
add(name = "suresh")
add(name = "vandana")

Default argument:-
----------------
it will take the default values from the arguments

num = 11
count = 0 
def prime(num,count):
    for j in range(1,num+1):
        if num % j == 0:
           count +=1
    if count == 2:
        print("prime number")
    else:
        print("not a prime number")
prime(num,count)

def prime(num,count):
    for j in range(1,num+1):
        if num % j == 0:
           count +=1
    if count == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
prime(num=11,count=0)
prime(num=17,count=0)
prime(num=19,count=0)
prime(num=21,count=0)

keyword argument:-
----------------

def any(cat,an,bog):
    print(f"an = {an},bog = {bog},cat = {cat}")
any(cat = 0,an = 11,bog = 19)

variable length arguments:-
-------------------------
 adding a (*) before the parameter name in the function, receive a tuple of argument and can acces index '''

def pink(*colour):
    print(colour[1])
pink("blue", "red", "green")  
    








