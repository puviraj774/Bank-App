#================================================================================================
from colorama import Fore, Back, Style, init
init(autoreset=True) 
# "pip install colorama" run in command prompt
import os
import random

#======================================================================================================
#============================== FUNCTION FOR ADMIN LOGIN VIEW ========================================
#======================================================================================================

def Admin_Menu(): 
    print('\n---------------------------------')
    print(Fore.GREEN+"======> Mini Banking Menu <======")
    print('---------------------------------\n\n')
    print(Fore.YELLOW+"1.Create Account")
    print(Fore.YELLOW+"2.Withdraw")
    print(Fore.YELLOW+"3.Deposit")
    print(Fore.YELLOW+"4.Check Balances")
    print(Fore.YELLOW+"5.Transfer Money")
    print(Fore.YELLOW+"6.Transaction History")
    print(Fore.YELLOW+"7.Search Account Details")
    print(Fore.RED+"8.Exit")

#======================================================================================================
#============================= FUNCTION FOR USER LOGIN VIEW ===========================================
#======================================================================================================

def User_Menu():  
    print('\n---------------------------------')
    print(Fore.GREEN+"======> Mini Banking Menu <======")
    print('---------------------------------\n\n')
    print(Fore.YELLOW+"1.Withdraw")
    print(Fore.YELLOW+"2.Deposit")
    print(Fore.YELLOW+"3.Check Balances")
    print(Fore.YELLOW+"4.Transfer Money")
    print(Fore.YELLOW+"5.Transaction History")
    print(Fore.RED+"6.Exit")

#==========================================================================================================
#============================ FUNCTION FOR CREATE ACCOUNT AND GET USER DETAILS ============================
#========================= AUTO ACCOUNT NUMBER CREATION AND AUTO USER NAME CREATION =======================
#==========================================================================================================

def Get_Valid_Info(Getinfo ="" ):
    while True:
        Value = input(Getinfo)
        if Value:
            return Value  
        else:
            print(Fore.RED+"Invalid Input . Enter Something !")


def Create_Account():
    
    Account_Numbers = list(range(1000,10000))
    random.shuffle(Account_Numbers)

    def Unique_Account_Num():
        if Account_Numbers:
            return Account_Numbers.pop()
        else:
            raise Exception("No more Unique Numbers!")
        
    try:
        with open("User_ID.txt",'r') as file: 
            Last_Acc = file.read().strip()
            New_Acc = int(Last_Acc[1:]) + 1
    except FileNotFoundError:       
        New_Acc = 2

    User_Id = "U"+str(New_Acc).zfill(3)
    with open ("User_ID.txt",'w') as file:
        file.write(User_Id)
    print(Fore.BLUE+"\n========> Create_Account <========\n")


    Acc_Holder_Name = Get_Valid_Info(f"{'Enter The Account Holder Name':<33} : ") 
    User_Address = Get_Valid_Info(f"{'Enter The Address':<33} : ")

    print(f"{'User Id':<33} : {User_Id}")

    while True:
        found = False
        User_Name = Get_Valid_Info(f"{'Enter The User Name':<33} : ")
        if os.path.exists("Users_Details.txt"):
            with open("Users_Details.txt",'r') as file: 
                for lines in file:
                    line = lines.strip().split(',')
                    if User_Name == line[1]:
                        found = True
                        break
                if  found:
                    print(Fore.RED+"Username Already Exists! Choose Different Username.")
                else:
                    break

    User_Password = Get_Valid_Info(f"{'Enter The Password':<33} : ")

    while True:
        try:
            balance = float(input(f"{'Enter The Initial Balance':<33} : RS "))
            break
        except ValueError:
            print(Fore.RED+"invalid input . Enter numbers Only!")
    

    print(Fore.YELLOW+"\nAccount Created Successfully!\n")  
    Account_Number = Unique_Account_Num()
    print(f"{'Account Number':<21} : {Account_Number}")
    print(f"{'User Id':<21} : {User_Id}")
    print(f"{'User Name':<21} : {User_Name}")
    print(f"{'User Password':<21} : {User_Password}")
    print(f"{'Initial Balance':<21} : Rs {balance}")

    with open ("Users_Details.txt",'a') as file: 
        file.write(f"{User_Id},{User_Name},{User_Password}\n")
    
    with open ("Customer_Details.txt",'a') as file: 
        file.write(f"{User_Id},{Acc_Holder_Name},{User_Address}\n")

    with open ("Account_Details.txt",'a') as file: 
        file.write(f'{Account_Number},{User_Id},{balance}\n')

    from datetime import datetime
    current_date_time = datetime.now()
    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

    with open('Transaction.txt','a') as file:
        file.write(f'{New_Date_Time},{Account_Number},Initial,{balance},{balance}\n')
#=======================================================================================================================
#=============================================== FUNCTION FOR WITHDRAW =================================================
#=======================================================================================================================
def Withdraw():
    global Account_Number
    found = False
    try:
        with open("Account_Details.txt", 'r') as file:
            for lines in file:
                line = lines.strip().split(',')

                if Account_Number == line[0]:
                    while True:
                        try:
                            Amount = float(input(f"Enter the Withdrawal Amount : Rs "))

                            if Amount > 0 and Amount <= float(line[2]):
                                New_Balance = float(line[2]) - Amount

                                with open("Account_Details.txt", 'r') as file:
                                    lines = file.readlines()

                                with open("Account_Details.txt", 'w') as file:
                                    for line in lines:
                                        details = line.strip().split(',')
                                        if details[0] == Account_Number:
                                            details[2] = str(New_Balance)
                                        file.write(f"{details[0]},{details[1]},{details[2]}\n")

                                from datetime import datetime
                                current_date_time = datetime.now()
                                New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

                                with open("Transaction.txt", 'a') as file:
                                    file.write(f"{New_Date_Time},{Account_Number},Withdraw,{Amount},{New_Balance}\n")

                                print(Fore.YELLOW+"\nWithdrawal Successful.\n")
                                print(f"{'Withdrawal Amount':<20} : Rs {Amount}")
                                print(f"{'New Balance':<20} : Rs {New_Balance}\n")
                                found = True
                                break
                            else:
                                print(Fore.RED+"\nInsufficient funds .Enter The Correct Amount!")
                                
                            if not found:
                                print(Fore.RED+"\nAccount Number Not Found!")

                        except ValueError:
                            print(Fore.RED+"\nInvalid input! Please enter a numeric value.")
                            
            if not found:
                print(Fore.RED+"\nAccount Number Not Found!")
    except FileNotFoundError:
        print(Fore.RED+"\nCreate customer first!")  

#======================================================================================================================
#===================================== FUNCTION FOR DEPOSIT ===========================================================
#======================================================================================================================

def Deposit(): #function for Deposit
    global Account_Number
    found = False
    try:
        with open("Account_Details.txt",'r') as file:
            for line in file:
                lines = line.strip().split(',')
                
                if Account_Number == lines[0]:
                    while True:
                        try:
                            Amount = float(input("Enter The Deposit Amount : Rs "))
                            if Amount > 0 :
                                New_Balance = float(lines[2]) + Amount
                                
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
                                    print(Fore.YELLOW+"\nWithdrawal Successful.\n")
                                    print(f"{'Deposit Amount':<16} : Rs {Amount}")
                                    print(f"{'New Balance':<16} : Rs {New_Balance}\n")
                                    found =  True
                                    break
                            else:
                                print(Fore.RED+"\nAmount Must be Greater Than Zero '0' .")
                        except ValueError:
                            print(Fore.RED+"\nEnter Numbers Only.")
                    break    
        if not found:
            print(Fore.RED+"\nAccount Number Not Found!")

    except FileNotFoundError:
        print(Fore.RED+"\nCreate Account First")
                
#========================================================================================================================
#===================================== FUNCTION FOR CHECK BALANCE =======================================================
#========================================================================================================================

def Check_Balance(): # function for check balance
    global Account_Number
    found_Account = False
    try:
        with open("Account_Details.txt",'r') as file:
            for line in file:
                datas = line.strip().split(',')

                if Account_Number == datas[0]:
                    print(f"\nAccount Balance is : Rs {float(datas[2])}\n")
                    found_Account = True
                    break
                    
            if not found_Account:
                print(Fore.RED+"Invalid Account Number !")
    except FileNotFoundError:
        print(Fore.RED+"file not found!")

#========================================================================================================================
#=================================== FUNCTION FOR TRANSACTION MONEY =====================================================
#========================================================================================================================

def Transaction(): #function for Transaction Money
    from datetime import datetime
    current_date_time = datetime.now()
    New_Date_Time = current_date_time.strftime("%d/%m/%y %H:%M")

    global Account_Number
    Account_Number2 = input(f"{'Transfer To':<15}: ")

    try:
        with open("Account_Details.txt",'r') as file:
            Acc01 = file.readlines()
        
        find_Account_Number =False
        find_Account_Number2 =False

        for line in Acc01:
            Details = line.strip().split(',')
            if Details[0] == Account_Number:
                find_Account_Number = True
                Balance01 = float(Details[2])
            if Details[0] == Account_Number2:
                find_Account_Number2 = True
                Balance02 = float(Details[2])
            

        if find_Account_Number and find_Account_Number2:
            while True:
                try:
                    Amount = float(input(f"\nEnter The Transfer Amount : Rs "))
                    if Amount <= Balance01 and Amount > 0:              

                        New_Balance01 = Balance01 - Amount
                        New_Balance02 = Balance02 + Amount
                    
                        with open("Account_Details.txt",'w') as file:
                            for up in Acc01:
                                update02 = up.strip().split(',')

                                if update02[0] == Account_Number:
                                    update02[2] = float(New_Balance01)
                                elif update02[0] == Account_Number2:
                                    update02[2] = float(New_Balance02)

                                file.write(f"{update02[0]},{update02[1]},{update02[2]}\n")
                            
                        with open("Transaction.txt",'a') as file:
                                    
                            file.write(f"{New_Date_Time},{Account_Number},Transfer out,{Amount},{New_Balance01}\n")
                            file.write(f"{New_Date_Time},{Account_Number2},Transfer In,{Amount},{New_Balance02}\n")
                            print(Fore.YELLOW+"\nTransaction Successful ! ")
                            break
                            
                    else :
                        print (Fore.RED+"\nInsufficient Funds! Enter The Correct Amount.")
                        
                except ValueError:
                    print(Fore.RED+"\nEnter Numbers Only!")
                    
        else:
            print(Fore.RED+"\nInvalid Account Number!")

    except FileNotFoundError:
        print(Fore.RED+"\nfile not found!")

#=========================================================================================================================
#=================================== FUNCTION FOR VIEW TRANSACTION HISTORY ===============================================
#=========================================================================================================================

def Transaction_History():  # function for transaction history
    global Account_Number

    try:
        with open("Transaction.txt", 'r') as file:
            lines = file.readlines()
            
            matched_lines = [line.strip().split(',') for line in lines if Account_Number == line.strip().split(',')[1]]

            if matched_lines:
                print(Fore.CYAN + Style.BRIGHT + (f"\n{'Date & Time' :<25}{'Account Number' :<20}{'Deposit / Withdraw' :<23}{'Amount':<10}{'Balance':<10}"))
                print('-' * 88)
                for line2 in matched_lines:
                    print(Fore.YELLOW + (f"{line2[0] :<25}{line2[1] :<20}{line2[2] :<23}{line2[3] :<10}{line2[4] :<10}\n"))
            else:
                print(Fore.RED + f"\nNo transactions found for account: {Account_Number}")

    except FileNotFoundError:
        print(Fore.RED + "Transaction file not found.")

#=======================================================================================================================
#================================== FUNCTION FOR SEARCH ACCOUNT DETAILS ================================================
#=======================================================================================================================

def Search_Account_Details():
    global Account_Number
    found = False

    try:
        with open("Account_Details.txt", 'r') as file:
            for line in file:
                account_data = line.strip().split(',')

        with open("Customer_Details.txt", 'r') as file2:
            for cust_line in file2:
                cust_data = cust_line.strip().split(',')

                if Account_Number == account_data[0]:
                    print (Fore.BLUE+"\nUser Details\n")
                    print(f"{'User ID':<25}: {account_data[1]}")
                    print(f"{'Account Balance':<25}: Rs {account_data[2]}")
                    found = True

                if cust_data[0] == account_data[1]:
                    print(f"{'Account holder Name':<25}: {cust_data[1]}")
                    print(f"{'User Address':<25}: {cust_data[2]}")
                    break 
                    
        if not found:
            print(Fore.RED+"\nAccount Not Found!")

    except FileNotFoundError:
        print(Fore.RED+"\nAccount Not Found!")

# ===============================================================================================
# ===========================         Program Start         ===================================== 
# ===============================================================================================

attempt =0
max_attempt = 3

while attempt < max_attempt:  

    if not os.path.exists("Users_Details.txt") or os.path.getsize("Users_Details.txt") == 0:
        print("Admin_UserName = Admin123\nAdmin_Password = pass123\n")
        with open ("Users_Details.txt",'w') as file:
            file.write("U001,Admin123,pass123\n")

    print(Fore.CYAN+Style.BRIGHT+"\n======Login======\n")

    username = input("Enter UserName : ")
    password = input("Enter Password : ")
   
    with open("Users_Details.txt",'r') as file:
        datas = file.readline()
        data = datas.strip().split(',')

    if username == data[1] and password == data[2]:
        print(Fore.CYAN+Style.BRIGHT+"\nLogin Successfully. WelCome Admin!")

        while True:
            Admin_Menu()

            choice = input("\nenter your opinion (1 - 8) : ")

            if choice == '1':
                Create_Account()

            elif choice == '2':               
                print(Fore.BLUE+"\n==========> Withdraw  <==========\n")
                Account_Number = input("Enter The Account Number : ")              
                Withdraw()

            elif choice == '3':
                print(Fore.BLUE+"\n==========> Deposit  <==========\n")
                Account_Number = input("Enter The Account Number : ")
                Deposit()

            elif choice == '4':                
                print(Fore.BLUE+"\n==========> Check Balance  <==========\n")
                Account_Number = input("Enter The Account Number : ")               
                Check_Balance()

            elif choice == '5':
                print(Fore.BLUE+"\n==========> Money Transfer  <==========\n")
                Account_Number = input(f"{'Transfer From':<15}: ")
                Transaction()

            elif choice == '6':
                print(Fore.BLUE+"\n==========>  View Transaction_History  <==========\n")
                Account_Number = input("Enter The Account Number : ")
                Transaction_History()

            elif choice == '7':
                print(Fore.BLUE+"\n==========>  Search Account Details  <==========\n")
                Account_Number = input("Enter The Account Number : ")
                Search_Account_Details()

            elif choice == '8':
                print(Fore.YELLOW+"Thank you for using Banking App. Exiting program!")
                exit()

            else:
                print(Fore.RED+"\nInvalid input!")

    else:
        try:
            with open ("Users_Details.txt",'r') as file:
                lines = file.readlines()
                found = False

                for line in lines:
                    line2 = line.strip().split(',')

                    if username  == line2[1] and  password == line2[2]:
                        userid = line2[0]
                        found = True

                        with open ("Account_Details.txt",'r') as file:
                            SAC = file.readlines()

                        for SAC2 in SAC:
                            SAC3 = SAC2.strip().split(',')
                            if userid == SAC3[1]:
                                Account_Number = SAC3[0]

                                print(Fore.CYAN+Style.BRIGHT+"\nLogin Successfully. WelCome !")
                                while True:
                                    User_Menu()

                                    choice = input("\nenter your opinion (1 - 6) : ")

                                    if choice == '1':
                                        print(Fore.BLUE+"\n==========> Withdraw  <==========\n")
                                        Withdraw()

                                    elif choice == '2':
                                        print(Fore.BLUE+"\n==========> Deposit  <==========\n")
                                        Deposit()

                                    elif choice == '3':
                                        print(Fore.BLUE+"\n==========> Check Balance  <==========\n")
                                        Check_Balance()

                                    elif choice == '4':
                                        print(Fore.BLUE+"\n==========> Money Transfer  <==========\n")
                                        Transaction()

                                    elif choice == '5':
                                        print(Fore.BLUE+"\n==========>  View Transaction_History  <==========\n")
                                        Transaction_History()

                                    elif choice == '6':
                                        print(Fore.YELLOW+"\nThank you for using Banking App. Exiting program!")
                                        exit()

                                    else:
                                        print(Fore.RED+"\nInvalid Input. Enter Between 1 to 6 ") 

                        break
        except FileNotFoundError:
            pass
    

    attempt += 1
    if attempt < max_attempt:
        print(Fore.RED+(f"\nLogin Failed You have only {max_attempt - attempt} attempt(s) left."))   
     
    if attempt == max_attempt:
        print(Fore.RED+(f"\nToo many Attempts Failed , Exiting Program.") ) 
        break 
     


           

                             

                         












