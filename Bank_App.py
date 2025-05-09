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
    print(f"{'User Name':<33} : {User_Id}")
    User_Password = input(f"{'Enter The Password':<33} : ")
    balance = float(input(f"{'Enter The Initial Balance':<33} : RS "))
    

    print("\nAccount Created Successfully!\n\n")  
    print(f"{'Account Number':<21} : {Account_Number}")
    print(f"{'Account Holder Name':<21} : {Acc_Holder_Name}")
    print(f"{'User Address' :<21} : {User_Address}")
    print(f"{'User Name':<21} : {User_Id}")
    print(f"{'User Password':<21} : {User_Password}")
    print(f"{'Initial Balance':<21} : Rs {balance}")

    with open ("Users_Details.txt",'a') as file:
        file.write(f"{User_Id},{User_Password}\n")
    
    with open ("Customer_Details.txt",'a') as file:
        file.write(f"{User_Id},{Acc_Holder_Name},{User_Address}\n")

    with open ("Account_Details.txt",'a') as file:
        file.write(f'{Account_Number},{Acc_Holder_Name},{balance}\n')

    from datetime import datetime
    current_date_time = datetime.now()
    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

    with open('Transaction.txt','a') as file:
        file.write(f'{New_Date_Time},{Account_Number},Deposit,{balance},{balance}\n')
#=======================================================================================================================

def Withdraw():
    global Account_Number

    with open("Account_Details.txt",'r') as file:
        line = file.readlines()
        for Acc_no in line:
            Acc_no02 = Acc_no.strip().split(',')
            if Account_Number == Acc_no02[0]:

                Amount = float(input("\nEnter the Withdrawal Amount : Rs "))

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

                    print(f"\nWithdrawal Successful.\n\nWithdrawal Amount : Rs {Amount}\nNew Balance : Rs {New_Balance}")
                    break
                else:
                    print("Invalid Amount or Insufficiand Funds!")
            else:
                print("Inavalid Account Number!")
#======================================================================================================================

def Deposit():
    global Account_Number
    
    with open("Account_Details.txt",'r') as file:
        line = file.readlines()
        for Acc_no in line:
            Acc_no2 = Acc_no.strip().split(',')
            if Account_Number == Acc_no2[0]:

                Amount = float(input("Enter The Deposit Amount : Rs "))

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

                    print(f"Deposit Successful.\nDeposit Amount : Rs {Amount}\nNew_Balance : Rs {New_Balance}")
                    break
                else:
                    print("Invalid Amount , Deposit must be greater than 0 ")
            else:
                print("Invalid Account Number!")
#========================================================================================================================
def Check_Balance():
    global Account_Number

    with open("Account_Details.txt",'r') as file:
        line = file.readlines()
       
        for Acc_no in line:
            Acc_no2 = Acc_no.strip().split(',')

    
            if Account_Number == Acc_no2[0]:
                print(f"\nAccount Balance is : Rs {float(Acc_no2[2])}\n")
                break
            
            else:
                print ("invalid Account Number❌ !") 
#========================================================================================================================
def Transaction():
    from datetime import datetime
    current_date_time = datetime.now()
    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

    global Account_Number
    Account_Number2 = input("\nEnter The Another Account Number To Transfer Amount : Rs ")


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
            break

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
                        Tran02[2] = "Transfer out"
                        Tran02[4] = float(New_Balance01)
                        Tran02[3] = Amount
                    if Tran02[1] == Account_Number2:
                        Tran02[2] = "Transfer In"
                        Tran02[4] = float(New_Balance02)
                        Tran02[3] = Amount
                        
                    file.write(f"{New_Date_Time},{Tran02[1]},{Tran02[2]},{Tran02[3]},{Tran02[4]}\n")
                    print("\nTransaction Successful ! ")

        else :
            print ("Insufficient Funds!")
    else:
        print("Invalid Account Number!")
#=========================================================================================================================
def Transaction_History():
    global Account_Number

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


with open ("Admin_Details.txt",'r') as file:
    Admin = file.readline().strip()

uname_for_admin , password_for_admin = Admin.split(',') 

username = input("Enter UserName : ")
password = input("Enter Password : ")


if username == uname_for_admin and password == password_for_admin:
    print("\nLogin Successfully. WelCome Admin!")
    while True:
        Admin_Menu()

        choice = input("\nenter your opinion (1 - 7) : ")

        if choice == '1':
            Create_Account()

        elif choice == '2':               
            print("\n==========> Withdraw  <==========\n\n")
            Account_Number = input("Enter The Account Number : ")              
            Withdraw()

        elif choice == '3':
            print("\n==========> Deposit  <==========\n\n")
            Account_Number = input("Enter The Account Number : ")
            Deposit()

        elif choice == '4':                
            print("\n==========> Check Balance  <==========\n\n")
            Account_Number = input("Enter The Account Number : ")               
            Check_Balance()

        elif choice == '5':
            print("\n==========> Money Transfer  <==========\n\n")
            Account_Number = input("Enter The Account Number : ")
            Transaction()

        elif choice == '6':
            print("\n==========>  View Transaction_History  <==========\n\n")
            Account_Number = input("\nEnter The Account Number : ")
            Transaction_History()

        elif choice == '7':
            print("Thank you for using ATM. Exiting program!")
            exit()
        else:
            print("\nInvalid input!")

else:
    try:
        with open ("Users_Details.txt",'r') as file:
            lines = file.readlines()

            for line in lines:
                line2 = line.strip().split(',')

                if username  == line2[0] and  password == line2[1]:

                    with open("Customer_Details.txt",'r') as file:
                        CUS = file.readlines()
                        for CUS2 in CUS:
                            CUS3 = CUS2.strip().split(',')
                            if CUS3[0] == line2[0]:
                                AHN = CUS3[1]
                                with open ("Account_Details.txt",'r') as file:
                                    SAC = file.readlines()

                                for SAC2 in SAC:
                                    SAC3 = SAC2.strip().split(',')
                                    if AHN == SAC3[1]:
                                        Account_Number = SAC3[0]

                                        print("\nLogin Successfully. WelCome !")
                                        while True:
                                            User_Menu()

                                            choice = input("\nenter your opinion (1 - 6) : ")

                                            if choice == '1':
                                                print("\n==========> Withdraw  <==========\n\n")
                                                Withdraw()

                                            elif choice == '2':
                                                print("\n==========> Deposit  <==========\n\n")
                                                Deposit()

                                            elif choice == '3':
                                                print("\n==========> Check Balance  <==========\n\n")
                                                Check_Balance()

                                            elif choice == '4':
                                                print("\n==========> Money Transfer  <==========\n\n")
                                                Transaction()

                                            elif choice == '5':
                                                print("\n==========>  View Transaction_History  <==========\n\n")
                                                Transaction_History()

                                            elif choice == '6':
                                                print("Thank you for using ATM. Exiting program!")
                                                exit()
                                            else:
                                                print("Invalid Input") 
       
    except FileNotFoundError:
        print("Login Failed! Try Again.")
        pass

           
            
               
                            

                         












