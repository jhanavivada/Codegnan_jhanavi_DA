'''table_num = int(input("enter the number"))
for j in range(1,11):
    print(f"{table_num} X {j} = {table_num * j}")
count(),capitalize(),isdescimal()join(),casefold(),strip()
,isalnum(),isupper(),replace(),isalpha(),split(),isdigit()

an = "PYThon is A ProGramMing LanguAGE"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper():
        count_U += 1
    elif ch.islower():
        count_L += 1
print(f"there are total{count_U} cap L")
print(f"there are total{count_L} small L")
program for cap and small 
an = "PYThon is A ProGramMing LanguAGE"
Cap_L = []
small_L = []
for ch in an:
    if ch.isupper():
        Cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f"{Cap_L} contain all Cap L")
print(f"{small_L} contain all small L")
program for atm 
SBI_janu_AC_details = {"name" : "janu",
                       "ATM PIN" : "1119"}
print("welcome to SBI ATM")
print("please insert your ATM card")
SBI_user_pin = input("please enter your 4 digits ATM pin: ")
if len(SBI_user_pin) == 4:
    if SBI_user_pin in SBI_janu_AC_details['ATM PIN']:
        print("the pin correct")
    else:
        print("you have enterted invalid pin")
else:
    print("please enter your 4 digit pin")

program for perfect number
per_num = int(input("enter the number"))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
   print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")
              
'''

        
