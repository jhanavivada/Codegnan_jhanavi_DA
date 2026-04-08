'''
Recursive functions :-
-------------------
Recursion is a programming technique where a function calls
itself either directly or indirectly to solve a problem by breaking it into smaller, simpler subproblems.
Recursion is especially useful for problems that can be  divided into identical smaller tasks,
such as mathematical calculations, tree traversals or divide-and-conquer algorithms.

def vaildate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("enter 4 digit PIN:")
        if len(user_pin)== 4 and user_pin == self.user_info["ATM PIN"]:
           print(" Welcome to the ATM")
           return True
        else:
            self.remaining_attempts -=1
            if self.remaining_attempts > 0:
                print(f"Invalid Pin. Attempts left: {sel:self.remaining}")
            else:
                print("card blocked. please contact customer care")
                return false
 
any = "I completed my b.tect in ECE"
vowel_word = []
con_word = []
def vowel_con(any,vowel_word,con_word):
    for j in any:
         if j in "AEIOUaeiou":
             vowel_word.append(j)
         else:
             con_word.append(j)
    print(f"{vowel_word} these are all vowel in the string")
vowel_con(any,vowel_word,con_word)          

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_list = []
non_prime_list = []

def prime_check(numbers, prime_list, non_prime_list):
    for num in numbers:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
            if is_prime:
                prime_list.append(num)
            else:
                non_prime_list.append(num)
        else:
            non_prime_list.append(num)
    print(f"{prime_list} these are prime numbers in the list")
prime_check(numbers, prime_list, non_prime_list)
'''


























                
                    
