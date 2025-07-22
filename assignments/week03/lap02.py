# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print("Your balance now :",balance)
        elif choice == "2":
            withdraw = float(input("Withdraw amount: "))
            if withdraw > balance:
                print("Your balance is not enough.")
                continue
            elif withdraw < 0:
                print("Withdraw can't less than 0 :")
                continue
            else:
                balance = balance - withdraw
                print("Withdraw successfully your balance now :",balance)
        elif choice == "3":
            deposit = float(input("Deposit amount: "))
            if deposit< 0:
                print("Deposit can't less than 0 :")
                continue
            else:
               balance = balance + deposit
               print("Deposit successfully your balance now :",balance)
        elif choice == "4":
            print("Thank you for using the ATM simulation.")
            break
        else:
            print("Your choice is worng")
            continue
else:
    print("Invalid PIN.")
