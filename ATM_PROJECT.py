SBI_janu_AC_details={"name":"janu","ATM PIN":"1119","Balance":5000}
while True:
    print("\n===== Welcome to SBI ATM =====")
    remaining_attempts=3
    while remaining_attempts>0:
        SBI_user_pin=input("Enter your 4 digit ATM PIN: ")
        if len(SBI_user_pin)==4 and SBI_user_pin.isdigit():
            if SBI_user_pin==SBI_janu_AC_details["ATM PIN"]:
                print("PIN correct")
                break
            else:
                remaining_attempts-=1
                if remaining_attempts>0:
                    print(f"Invalid PIN, attempts left:{remaining_attempts}")
                else:
                    print("You've run out of attempts, your card is blocked")
                    break
        else:
            print("Please enter 4 digit PIN")
    if remaining_attempts==0:
        break
    user_choice=int(input("Enter:\n1.Withdraw\n2.Deposit\n3.Check Balance\n4.Change PIN\n5.Exit\n"))
    if user_choice==1:
        money_w=int(input("Enter amount: "))
        if money_w<=SBI_janu_AC_details["Balance"]:
            SBI_janu_AC_details["Balance"]-=money_w
            print("Balance:",SBI_janu_AC_details["Balance"])
        else:
            print("Insufficient balance")
    elif user_choice==2:
        deposit_m=int(input("Enter amount: "))
        if deposit_m%100==0 and deposit_m>=100:
            SBI_janu_AC_details["Balance"]+=deposit_m
            print("Deposit successful")
            print("Balance:",SBI_janu_AC_details["Balance"])
        else:
            print("Invalid amount")
    elif user_choice==3:
        print("Balance:",SBI_janu_AC_details["Balance"])
    elif user_choice==4:
        attempts=3
        while attempts>0:
            old_pin=input("Enter old PIN: ")
            if old_pin==SBI_janu_AC_details["ATM PIN"]:
                new_pin=input("Enter new 4 digit PIN: ")
                if len(new_pin)==4 and new_pin.isdigit():
                    SBI_janu_AC_details["ATM PIN"]=new_pin
                    print("PIN changed successfully")
                    break
                else:
                    print("Invalid new PIN")
            else:
                attempts-=1
                print("Wrong PIN, attempts left:",attempts)
        continue
    elif user_choice==5:
        print("Thank you")
        break
    else:
        print("Invalid choice")
    
        


