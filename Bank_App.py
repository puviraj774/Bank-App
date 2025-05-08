#================================================================================================
from ntpath import join


def Admin_Menu(): #Function For Admin Login view 
    print('\n---------------------------------')
    print("======> Mini Banking Menu <======")
    print('---------------------------------\n\n')
    print("1.Create Account")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Check Balances")
    print("5.Transfer Money")
    print("6.Transaction History")
    print("7.Exit")
    
#======================================================================================================
def User_Menu():  #Function For User login view
    print('\n---------------------------------')
    print("======> Mini Banking Menu <======")
    print('---------------------------------\n\n')
    print("1.Withdraw")
    print("2.Deposit")
    print("3.Check Balances")
    print("4.Transfer Money")
    print("5.Transaction History")
    print("6.Exit")

#======================================================================================================

def Create_Account():#Function For Create Account 
      
    try:
        with open("Acc_No.txt",'r') as file: # Auto Create Account Numbers
            Last_Acc = file.read().strip()
            New_Acc = int(Last_Acc[1:]) + 1
    except FileNotFoundError:       
        New_Acc = 1

    Account_Number = "A"+str(New_Acc).zfill(3)
    with open ("Acc_No.txt",'w') as file:
        file.write(Account_Number)

    try:
        with open("User_ID.txt",'r') as file: # Auto Create Account Numbers
            Last_Acc = file.read().strip()
            New_Acc = int(Last_Acc[1:]) + 1
    except FileNotFoundError:       
        New_Acc = 1

    User_Id = "U"+str(New_Acc).zfill(3)
    with open ("User_ID.txt",'w') as file:
        file.write(User_Id)

    print("\n----------------------------------")
    print("========> Create_Account <========")
    print("----------------------------------\n\n")

    Acc_Holder_Name = input(f"{'Enter The Account Holder Name':<33} : ") # Getting Input from user
    User_Address = input(f"{'Enter The Address':<33} : ")
    User_Phone_Number = int(input(f"{'Enter The Phone Number':<33} : "))
    User_Name = input(f"{'Enter The User Name':<33} : ")
    User_Password = input(f"{'Enter The Password':<33} : ")
    balance = float(input(f"{'Enter The Initial Balance':<33} : RS "))
    

    print("\nAccount Created Successfully!\n\n")  
    print(f"{'Account Number':<21} : {Account_Number}")
    print(f"{'Account Holder Name':<21} : {Acc_Holder_Name}")
    print(f"{'User Address' :<21} : {User_Address}")
    print(f"{'User Phone Number' :<21} : {User_Phone_Number}")
    print(f"{'User Name':<21} : {User_Name}")
    print(f"{'User Password':<21} : {User_Password}")
    print(f"{'Initial Balance':<21} : Rs {balance}")

    with open ("Users_Details.txt",'a') as file:
        file.write(f"{User_Id},{User_Name},{User_Password}\n")
    
    with open ("Customer_Details.txt",'a') as file:
        file.write(f"{User_Id},{Acc_Holder_Name},{User_Phone_Number},{User_Address}\n")

    with open ("Account_Details.txt",'a') as file:
        file.write(f'{Account_Number},{Acc_Holder_Name},{balance}\n')

    from datetime import datetime
    current_date_time = datetime.now()
    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

    with open('Transaction.txt','a') as file:
        file.write(f'{New_Date_Time},{Account_Number},Deposit,{balance},{balance}\n')
#=======================================================================================================================

def Withdraw():
    Account_Number = input("Enter The Account Number : ")

    with open("Account_Details.txt",'r') as file:
        line = file.readlines()
        for Acc_no in line:
            Acc_no02 = Acc_no.strip().split(',')
            if Account_Number == Acc_no02[0]:

                Amount = float(input("Enter the Withdrawal Amount : $ "))

                if Amount > 0 and Amount <= float(Acc_no02[2]):

                    New_Balance = float(Acc_no02[2]) - Amount

                    with open("Account_Details.txt",'r') as file:
                        lines = file.readlines()

                    with open("Account_Details.txt",'w') as file:
                        for line in lines:
                            details = line.strip().split(',')
                            if details[0] == Account_Number:
                                details[2] = New_Balance
                            file.write(f"{details[0]},{details[1]},{details[2]}\n")

                    from datetime import datetime
                    current_date_time = datetime.now()
                    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

                    with open ("Transaction.txt",'a') as file:
                        file.write(f"{New_Date_Time},{Account_Number},Withdraw,{Amount},{New_Balance}\n")

                    print(f"Withdrawal Successful.\nWithdrawal Amount : ${Amount}\nNew Balance : Rs {New_Balance}")
                else:
                    print("Invalid Amount or Insufficiand Funds!")
            else:
                print("Inavalid Account Number!")
#======================================================================================================================

def Deposit():
    Account_Number = input("Enter The Account Number : ")

    with open("Account_Details.txt",'r') as file:
        line = file.readlines()
        for Acc_no in line:
            Acc_no2 = Acc_no.strip().split(',')
            if Account_Number == Acc_no2[0]:

                Amount = float(input("Enter The Deposit Amount : $ "))

                if Amount > 0 :
                    New_Balance = float(Acc_no2[2]) + Amount
                    
                    with open("Account_Details.txt",'r') as file:
                        lines = file.readlines()

                    with open("Account_Details.txt",'w') as file:
                        for line in lines:
                            details = line.strip().split(',')
                            if details[0] == Account_Number:
                                details[2] = New_Balance
                            file.write(f"{details[0]},{details[1]},{details[2]}\n")

                    from datetime import datetime
                    current_date_time = datetime.now()
                    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

                    with open ("Transaction.txt",'a') as file:
                        file.write(f"{New_Date_Time},{Account_Number},Deposit,{Amount},{New_Balance}\n")

                    print(f"Deposit Successful.\nDeposit Amount : {Amount}\nNew_Balance : Rs {New_Balance}")
                else:
                    print("Invalid Amount , Deposit must be greater than 0 ")
            else:
                print("Invalid Account Number!")
#========================================================================================================================
def Check_Balance():
    Account_Number = input("Enter The Account Number : ")

    with open("Account_Details.txt",'r') as file:
        line = file.readlines()
       
        for Acc_no in line:
            Acc_no2 = Acc_no.strip().split(',')

    
        if Account_Number == Acc_no2[0]:
            print(f"Account Balance is : Rs {float(Acc_no2[2])}")
        
        else:
            print ("invalid Account Number !") 
#========================================================================================================================
def Transaction():
    from datetime import datetime
    current_date_time = datetime.now()
    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

    Account_Number = input("Enter The Account Number : ")
    Account_Number2 = input("Enter The Another Account Number To Transfer Amount :")


    with open("Account_Details.txt",'r') as file:
        Acc01 = file.readlines()
    
    find_Account_Number =False
    find_Account_Number2 =False

    for line in Acc01:
        Details = line.strip().split(',')
        if Details[0] == Account_Number:
            find_Account_Number = True
            Balance01 = float(Details[2])
        elif Details[0] == Account_Number2:
            find_Account_Number2 = True
            Balance02 = float(Details[2])

    if find_Account_Number and find_Account_Number2:
        Amount = float(input("Enter The Amount :"))
        if Amount <= Balance01:                

            New_Balance01 = Balance01 - Amount
            New_Balance02 = Balance02 + Amount

            with open("Account_Details.txt",'r') as file:
                update01 = file.readlines()
            
            with open("Account_Details.txt",'w') as file:
                for up in update01:
                    update02 = up.strip().split(',')
                    if update02[0] == Account_Number:
                        update02[2] = float(New_Balance01)
                    if update02[0] == Account_Number2:
                        update02[2] = float(New_Balance02)
                    file.write(f"{update02[0]},{update02[1]},{update02[2]}\n")

            with open ("Transaction.txt",'r') as file:
                Tran01 = file.readlines()
            
            with open("Transaction.txt",'a') as file:
                for Trans in Tran01:
                    Tran02 = Trans.strip().split(',')
                    if Tran02[1] == Account_Number:
                        Tran02[2] = "Withdraw"
                        Tran02[4] = float(New_Balance01)
                        Tran02[3] = Amount
                    if Tran02[1] == Account_Number2:
                        Tran02[2] = "Deposit"
                        Tran02[4] = float(New_Balance02)
                        Tran02[3] = Amount
                        
                    file.write(f"{New_Date_Time},{Tran02[1]},{Tran02[2]},{Tran02[3]},{Tran02[4]}\n")

        else :
            print ("Insufficient Funds!")
    else:
        print("Invalid Account Number!")
#=========================================================================================================================
def Transaction_History():
    Account_Number = input("\nEnter The Account Number : ")

    try:
        with open("Transaction.txt",'r') as file:
            lines = file.readlines()
            print(f"\n{'Date & Time' :<25}{'Account Number' :<20}{'Deposit / Withdraw' :<23}{'Amount':<10}{'Balance':<10}")
            print('-' * 88)
                
            for line in lines:
                line2 = line.strip().split(',')
                if Account_Number == line2[1]:
                    print(f"{line2[0] :<25}{line2[1] :<20}{line2[2] :<23}{line2[3] :<10}{line2[4] :<10}\n")


        
                

    except FileNotFoundError:

        print("file not found")
# ===============================================================================================
# ===========================   ☠️      Program Start    ☠️     ================================
# ===============================================================================================
Admin_Details = 'Admin123,pass123\n'

with open ("Admin_Details.txt",'w') as file:
    file.write(Admin_Details)



print("\n======Login======\n")

attempt = 0
max_attempt = 3

while attempt < max_attempt:

    with open ("Admin_Details.txt",'r') as file:
        Admin = file.readline().strip()
    
    uname_for_admin , password_for_admin = Admin.split(',') 
    
    username = input("Enter UserName : ")
    password = input("Enter Password : ")


    if username == uname_for_admin and password == password_for_admin:
        print("\nLogin Successfully. WelCome Admin!")
        while True:
            Admin_Menu()

            choice = input("\nenter your opinion (1 - 6) : ")

            if choice == '1':
                Create_Account()

            elif choice == '2':
                Withdraw()

            elif choice == '3':
                Deposit()

            elif choice == '4':
                Check_Balance()

            elif choice == '5':
                Transaction()

            elif choice == '6':
                Transaction_History()

            elif choice == '7':
                print("Thank you for using ATM. Exiting program!")
                exit()
            else:
                print("Invalid input!")

    else:
        with open ("Users_Details.txt",'r') as file:
            lines = file.readlines()

            for line in lines:
                line2 = line.strip().split(',')

            
                if username  == line2[1] and  password == line2[2]:
                    print("\nLogin Successfully. WelCome !")
                    while True:
                        User_Menu()

                        choice = input("\nenter your opinion (1 - 5) : ")

                        if choice == '1':
                            Withdraw()

                        elif choice == '2':
                            Deposit()

                        elif choice == '3':
                            Check_Balance()

                        elif choice == '4':
                            Transaction()

                        elif choice == '5':
                            Transaction_History()

                        elif choice == '6':
                            print("Thank you for using ATM. Exiting program!")
                            exit()
                        else:
                            print("Invalid Input") 
                else:
                    attempt += 1
                    if max_attempt == attempt:
                        print("too many attempts failed. exiting program!")
                        exit() 
                    else:    
                        print(f"Login failed . you have only {max_attempt - attempt} attempts left.")                   

                         


    
       





            



















