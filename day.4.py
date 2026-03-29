'''
print(9+6)
print("Python" + "Language")
print([2+3] + [4+5])

concatenation
-------------
this is nothig but, a (+) behavi..
case-1:-
intergers---this will act as addtion for the int

case-2:-
for other datatypes (we have to use same type) this (+) act as concatention
if we try to access 2 different types, it can only concatent , only string to string  

print(9+6)
print("jhanavi" + "naidu")
print([2+3] + [4+5])
      
tuple()---> it is collection of different data types and this is represented by () and then seprated by (,)
eg...
thing = (11,"janu",[18,23],(4,6))

thing = (11,"janu",[18,23],(4,6))
print(thing)

thing = (12,89,"python",(23,"janu",[67,"python is a language",(7,8)],[8,("python"),[34,9]]))
print(thing[3][2][1][9])

num = 11
num_2 = 19
print(f"before swapping num = {num} and num_2 = {num_2}")
num, num_2 = num_2, num
print(f"after swapping num = {num} and num_2 = {num_2}")
'''
leap_year = int(input("enter year:"))
if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
   print(f"yes, {leap_year} is a leap year")
else:
     print(f"no, {leap_year} is not a leap year")











