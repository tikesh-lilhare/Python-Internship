import time
print("Create ATM Machine Using Python")
print("***************************************************")
print("Welcome To XYZ ATM !!")

print("Please Insert Your Credit/Debit Card !")
time.sleep(5)
password = 12345


pin = int(input("Enter Your Pin :"))

balance = 10000

if pin == password:
    while True:


        print("""
                1 == Balance Inquiry
                2 == Withdrawl Amount
                3 == Deposit Amount 
                4 == Exit
            """)
        
        try:
            option=int(input("Please Enter Your Choice :"))
        except:
            print("Please Enter Valid Option :")




        if option == 1:
            print("Your Current Balance Is",balance)

        if option == 2:
            
            withdrawl = int(input("Enter Withdrawl Amout :"))
            balance = balance - withdrawl
            print("After Withdrawl, Your Remaining Balance Is :",balance)

        if option == 3:
            deposit = int(input("Enter Deposit Amount:"))
            balance += deposit
            print("Your Balance After Deposit :",balance)


        if option == 4:
            break
else :
    Print("Please Enter Correct Pin")

