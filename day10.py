   '''List Methods:
Add → append(), extend(), insert()
Remove → remove(), pop(), clear()
Check → index(), count()
Arrange → sort(), reverse()
Copy → copy()

append():-
--------
nums = [8, 11, 19]
nums.append(39)
print(nums)

extend():-
-------
nums = [11, 22]
nums.extend([33, 44, 55])
print(nums)

insert():-
-------
nums = [1, 2, 4]
nums.insert(2, 3)
print(nums)

remove():-
--------
nums = [8, 11, 19, 39]
nums.remove(39)
print(nums)

pop():-
----
nums = [10, 20, 30]
nums.pop(1)
print(nums)

clear():-
-----
nums = [23, 29, 32]
nums.clear()
print(nums)

index():-
-----
nums = [10, 20, 30]
print(nums.index(20))

count():-
-----
nums = [1, 2, 2, 3, 2]
print(nums.count(2))

sort():-
-----
nums = [25563, 716753, 93236, 13512]
nums.sort()
print(nums)

reverse():-
-------
nums = [11, 23, 35]
nums.reverse()
print(nums)

copy():-
-----
nums = [1, 2, 3]
new_list = nums.copy()
print(new_list)

for triangle:-
------------
num = int(input("enter the limit"))
for j in range(num):
    for i in range (j):
        print(j,end = "")
    print()

for square:-
----------
num = int(input("enter the limit"))
for j in range(num):
    for i in range(num):
        print("*", end="")
    print()
for revers triangle
num = int(input("enter the limit"))
for j in range(num, 0, -1):
    for i in range(j):
        print("#", end="")
    print()

OR

num = int(input("enter the limit"))
for j in range(num):
    for i in range(num-j):
        print("#", end="")
    print()
    
pyrmaid:-
-------
num = int(input("enter the limit"))
for j in range(num):
         print(" " *(num-j),end = "")
         for i in range(j+1):         
             print("*",end= " ",)
         print()

fuction :-
for triangle:-

  def print_pattern():
    num = int(input("enter the limit: "))
    
    for j in range(num):
        for i in range(j):
            print(j, end="")
        print()
print_pattern()  
 
for square:-
          
def print_square(num):
    for j in range(num):
        for i in range(num):
            print("#", end="")
        print()
num = int(input("enter the limit: "))
print_square(num)

pyrmaid:-

def print_pattern(num):
    for j in range(num):
        print(" " * (num - j), end="")
        for i in range(j + 1):
            print("$", end=" ")
        print()
num = int(input("enter the limit: "))
print_pattern(num)  

prime number using count:-
'''
def check_prime(num):
    count = 0
    
    for j in range(1, num + 1):
        if num % j == 0:
            count += 1
    
    if count == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
prime_num = int(input("enter the number: "))
check_prime(prime_num)
















