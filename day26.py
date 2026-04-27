'''
Regular Expressions(RegEx):-
-------------------------
-->This regular experssion or RegEx is a squence of characters that forms a searching pattern.
-->To use this we have to import re, which will unlock the package

Functions:-
---------
1.findall
2.search

1.findall:-
  -------
-->By using this function, it will find all sequence in the string
syntax-->re.findall("metachar",variable_name)
ex:-
import re
any = "Python is a programing language"
so = re.findall("a",any)
print(so)

2.search:-
  ------
-->It will only find first sequence in the string
syntax-->re.search("metachar",variable_name)
ex:-
import re
any = "Python is a programing language"
so = re.search("a",any)
print(so)

Metacharacters:-
--------------
Metacharacters are used to form searching pattern

1.[]:-
  In this meta character we can search for [a-z],[A-z],[0-9]

import re
any = "0This regular experssion or RegEx is1 a squence of characters That forms a searching paTtern9"
far = re.findall("[a-s]",any)
has = re.search("[a-s]",any)
print(far)
print(has)

2.Dot(.):-
-->This meta charater will form a searchig pattern as it will take any single character for (.) 

import re
we ="Hello"
the = re.findall("H...o",we)
print(the)

import re
we ="Hello"
was = re.search("He..o",we)
print(was)

3.^
This is used to find the string is starting with the sequence or not
syntax:-re.findall("metachar",variable_name)

import re
how = "This is a meta charater will form a searchig pattern as it will take any single character for"
where = re.findall("^This is",how)
print(where)

import re
how = "This meta charater will form a searchig pattern as it will take any single character for"
where = re.search("^This",how)
print(where)

4.$:-
This is used to find the string is ending with the sequence or not
syntax:-re.findall("$",variable_name)

import re
janu = "This is used to find the string is ending with the sequence or not"
jhanavi = re.findall("not$",janu)
satya = re.search("not$",janu)
print(jhanavi)
print(satya)

5.*:-
This meta charater will form a searchig pattern as it will take any zero or more character for (*)
syntax:- re.findall(".*",variable_name)

import re
janu = "This is meta used to find the string is ending with the sequence or not"
jhanavi = re.findall("m.*e",janu)
satya = re.search("T.*",janu)
print(jhanavi)
print(satya)

6.+:-
This meta charater will form a searchig pattern as it will take any one or more character for (+)
syntax:- re.findall(".+",variable_name)'''
import re
janu = "This is meta used to find the string is ending with the sequence or not"
jhanavi = re.findall("s.+e",janu)
satya = re.search("T.+",janu)
print(jhanavi)
print(satya)
