#for stopping program execution for some time
import time

print("Please insert Your CARD")
print(" .")
time.sleep(1)
print(" .")
time.sleep(1)
print(" .")
time.sleep(1)
print(" .")
time.sleep(1)
print(" .")
time.sleep(1)

#for card processing
# time.sleep(5)

password = 1234

#taking atm pin from user
pin = int(input("Enter your ATM pin "))

#user account balance
balance = 5000

#checking pin is valid or not 
if pin == password:
    #loop will run user get free 
    while True:

        #Showing  info to user

        print(""" 
			1 == Check your Balance
			2 == Withdraw money
			3 == Deposit money
			4 == Exit
			"""
              )

        try:    
             #taking an option from user
            option = int(input("Please Enter your Choice "))
        except:
            print("Please Enter valid Option")
        
        #for option 1        
        if option == 1:
            print(f"Your current balance is {balance}")
                                     
        if option == 2:

            withdraw_amount = int(input("Please Enter withdraw amount : "))

            

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            

            print(f"Your updated balance is {balance}")

            

        if option == 3:

            deposit_amount = int(input("Please Enter deposit amount"))

            balance = balance + deposit_amount

            

            print(f"{deposit_amount} is credited to your account")



            print(f"Your updated balance is {balance}")



        if option == 4:

            break


else:
    print("Wrong Pin ! Please try again ......")
