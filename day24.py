'''
Handling Error:-
--------------
try bock --> try block will test a block of code for error
ex:-
try:
  print(b)

Except block:-
------------
-->This block will take care of any error
ex:-
except:
    print("This block can handle error")
    
Else block:-
----------
-->else keyword to defind a block of code to be excuted if no error were raied

try:
    num_1 = 11
    num_2 = 19
    print(num_1 ^ num_2)
except:
    print("There is a error")
else:
    print("everything is ok")

try:
    num_1 = 11
    num_2 = 19
    print(num_1 ^ num_2 ^ num_3)
except:
    print("There is a error")
else:
    print("everything is ok")
    

Finally block:-
-------------
-->This block will excute either try block have any error or no error


try:
  num_1 = 19
  num_2 = 11
  print(num_1+num_3)

except:
  print("error here")
else:
    print("No error in the code")
finally:
    print("the try-except block is finished")


try:
  num_1 = 19
  num_2 = 11
  print(num_1+num_2)

except:
  print("error here")
else:
    print("No error in the code")
finally:
    print("the try-except block is finished")

try:
    num1 = 10   
    num2 = 2    
    print(num1 / num2)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
else:
    print("Result")
finally:
    print("Everything is ok")

try:
    num1 = 10
    num2 = 2
    result = num1 / num2
    print(result + x)  
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except NameError:
    print("Variable not defined")
else:
    print("Result")
    '''
try:
    num1 = int(input("Enter the number:"))
    num2 = int(input("Enter the number:"))
    result = num1 / num2
    print(result)  

    exec("print('Hello'")   

except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except NameError:
    print("Variable not defined")
except SyntaxError:
    print("Syntax is wrong")
else:
    print(f"Result = {result}")
finally:
    print("Everything done properly")
