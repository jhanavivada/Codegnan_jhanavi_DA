'''
Modules
-------
-->A module in a python is simple file that contain python code(Function,variable,classes)
-->To use modules, we have to use a keyword called import before the module

Types of functions:-
------------------
1.Built-in or inbuilt
2.User-define modules

2.User-define modules:-
---------------------
--> this is developed by the user or programmer inside a file
of python code and used by calling import with filename

syntax :- import(keyword) file_name
          file_name.functionality
       
ex:
import day3
print(day3.List_1)

1.Built-in or inbuilt:-
---------------------
--> Already these are comes with installation and they are ready to use in the program
--> This is developed by the developer
ex:- Os,Math....

syntax:-
------
import(keyword) module_name
module_name.functionality

import math
print(math.tan(1))
'''
import random

def game():
    num = random.randint(1, 10)
    chances = 3

    while chances > 0:
        guess = int(input("Guess number (1-10): "))

        if guess == num:
            print("You win ")
            return
        else:
            chances -= 1
            print("Wrong! Left:", chances)

    print("You lost  Number was:", num)
game()
                    
                        
                    
      
