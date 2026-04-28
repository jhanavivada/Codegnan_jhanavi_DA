'''
Special sequence:-
----------------
A Special sequence is a \ followed by the one of the char in the list menu and has a special meaning
1.\A:-
-->Return a match if the specified characters are at the beginning of the string
ex:- "\AThe"

import re
word = "Janu is a good girl"
has = re.findall("\AJanu",word)
was = re.search("\AJanu",word)
print(has)
print(was)
if has:
    print("Yes, there is a match")
else:
    print("No Match")

2.\b:-
-->Return a match where the specified characters are at the beginning or at the end of the word
ex:-r"\bain"

import re
we = "Have a good day"
has = re.findall(r"\bday",we)
have = re.search(r"\bday",we)
print(has)
print(have)
if has:
    print("There")
else:
    print("Not there")
if have:
    print("There")
else:
    print("Not there")

3.\d:-
-->Return a match where the string contain digit(number from 0-9)
ex:-"\d"

import re
am = "Today temp is 40"
he = re.findall("\d",am)
she = re.search("\d",am)
print(he)
print(she)
if he:
    print("There")
else:
    print("Not there")
if she:
    print("There")
else:
    print("Not there")

4.\D:-
-->return a match where the string DOES NOT contain digits
Ex:-"\D"

import re
am = "Today temp is 40"
he = re.findall("\D", am)
she = re.search("\D", am)
print(he)
print(she)
if he:
    print("There")
else:
    print("Not there")
if she:
    print("There")
else:
    print("Not there")

5.\s:-
-->return a match where the string contains a white space
ex:- "\s"

import re
was = "hii hello how are you"
has = re.findall("\s",was)
had = re.search("\s",was)
print(has)
print(had)
if has:
    print("Match")
else:
    print("No match")
if had:
    print("Match")
else:
    print("No match")

6.\S:-
-->return a match where the string DOES NOT contains a white space character
ex:- "\S"

import re
was = "hii hello how are you"
has = re.findall("\S",was)
had = re.search("\S",was)
print(has)
print(had)
if has:
    print("Match")
else:
    print("No match")
if had:
    print("Match")
else:
    print("No match")

Time and Date :-
-------------
%d ---> Day
%m ---> Month
%Y ---> Year
%H ---> Hour
%M ---> Min
%s ---> Sec
%p ---> M/PM
%A ---> Day name
%B ---> Month name

import datetime
now = datetime.datetime.now()
print(now)
'''
import datetime
today = datetime.date.today()
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))


