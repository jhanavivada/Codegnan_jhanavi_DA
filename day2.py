'''string--> string is a collation of char,which represter by "" or '' and we can access the using
indexing( string can also allow negative indexing)
and also slicing this is also immutable,where i could not able to modify on the paticular vari
    print(any[3,4])
TypeError: string indices must be integers, not 'tuple'
 
any = 'vada jhanavi'
so = any.replace("vada","satya")
print(any[-3])
print(so)
len()--> len() method is used to get char present in the structer or find the length of the string

note:- we can covert a string into integer, if the string contain only integer values...

a_day="i'm jhanavi from vizag, has completed my b.tect"
print(f'(my name is {a_day[-23:-1]}) 

a_day="i'm jhanavi from vizag, has completed my b.tect"
print(len(a_day))

methods of string:-
-----------------
split()---> remove space,and the is in the list[] it will give the seprated thing in each index
syntax----> variable_name.split("substring")

lower()---> this is used to convert all letters into lower case 
syntax---> variable_name.lower()

some ="janu is a good girl"
print(some.split())

some ="java is very hard"
print(some.split("hard"))

some=" jaVa iS Hard"
print(some.lower())

some=" jaVa iS Hard"
print(some.upper())

replace()--->this used to replace old str with the new str
syntax---> variable_name.replace("old string","new string")

some = "python is a programming language"
print(some.replace("programming","normal"))

some = "python is a programming language"
if "python" in some:
    print("yes")
else:
    print("no")
'''

