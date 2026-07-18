balance=1000
password=1221
pin=int(input("ENTER YOUR PIN:"))
if pin==password:
    print("===ENTERED CORRECT PIN.===")
    
    while True:
        print("\n1.CHECK BALANCE.")
        print("2.DEPOSIT.")
        print("3.WITHDRAW.")
        print("4.EXIT.")

        choice=int(input("CHOICE AN OPTION:"))

        if choice==1:
            print("===AVALIABLE BALANCE: ===",balance)

        elif choice==2:
            amount=int(input("ENTER AMOUNT TO DEPOSIT:"))
            balance+=amount
            print("===AMOUNT DEPOSITED SUCCESSFULLY.===")
        elif choice==3:
            amount=int(input("ENTER AMOUNT TO WITHDRAW:"))
            if amount<=balance:
                balance-=amount
                print("===AMOUNT WITHDRAWED SUCCESSFULLY.===")
            else:
                print("===INSUFFICIENT BALANCE===")
        elif choice==4:
            print("===THANK YOU.===")
            break
        else:
            print("===INVALID CHOICE.===")
        
else:
    print("===INCORRECT PIN.===")