# importing important modules
import random 
import numpy

class Account:
    depositFrequency = 4
    transactionMax = 40000
   # Construct an Account object. Mde to
    def __init__(self, id, balance = 0, withdrawalDailyMax = 50000,
    withdrawalFrequency=3,withdrwalTransactionMax=20000, depoDailyMax = 150000, 
    depositFrequency = 4, depoTransactionMax = 40000):
        self.id = id
        self.balance = balance
        # withdral
        self.withdrawalDailyMax = withdrawalDailyMax
        self.withdrawalFrequency=withdrawalFrequency
        self.withdrwalTransactionMax=withdrwalTransactionMax
        # deposit
        self.depoDailyMax=depoDailyMax
        self.depositFrequency = depositFrequency
        self.depoTransactionMax=depoTransactionMax

    def getId(self):
        return self.id
#  a function to get balance
    def getBalance(self):
        return self.balance
        # getters for withdrwal 
    def getWithdrawalFrequency(self):
        return self.withdrawalFrequency
    def getWithdrwalTransactionMax(self):
        return self. withdrwalTransactionMax
    def getWithdrawalDailyMax(self):
        return self.withdrawalDailyMax
# getters for depo
    def getDepoDailyMax(self):
        return self.depoDailyMax
    def getDepositFrequency(self):
        return self.depositFrequency
    def getDepoTransactionMax(self):
        return self.depoTransactionMax

#  a function to withdraw
    def withdraw(self, amount):
    #    here if you withdraw your new balance changes
        self.balance -= amount
#  a function to depoit
    def deposit(self, amount):
    #    deposit equals amount being deposited+existing balance
        self.balance += amount 

#  a function to quit coming later

def main():
    # Creating accounts 
    accounts = []
    for i in range(1000, 9999): 
        account = Account(i, 0)
        accounts.append(account)    
    # ATM Processes
    while True:
       # Reading id from user which represents a secret pin for security
        id = int(input("\n Please Enter Your account pin: "))
       # Loop till id is valid between 1000 and 9999 in a randomised manner(where the Random module come in)
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid Pin.. Re-enter your Pin please: "))

        # while the pin is right(Id is pin here)
        while True:
            # Printing menu
            print("\n1 - Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Quit ")

            # Reading selection
            selection = int(input("\nEnter your selection: "))
            # Getting account object
            for acc in accounts:
                # Comparing account id
                if acc.getId() == id:
                    accountObj = acc
                    break
                   # View Balance
            if selection == 1:
               # Printing balance
                print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
             # Withdraw
            elif selection == 2:
                print("Your Balance is:" + str(accountObj.getBalance()))
               # Reading amount
                amt = float(input("\nPlease Enter amount to withdraw: "))
                ver_withdraw = input("Is this the correct amount, Yes or No ? " + str(amt) + " ")
    
                if ver_withdraw == "Yes":
                    print("Verify withdraw")
                else:
                    break

                if amt < accountObj.getBalance():
                    print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
                    # Calling withdraw method
                    accountObj.withdraw(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                    print("you have only 2 withdrawal times remaining")
                else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " \n")
                    print("\nPlease make a deposit.")
             # Deposit
            elif selection == 3:
                
                print("Your Balance is:" +  str(accountObj.getBalance())+ " ")
                # Reading amount
                amt = float(input("\nEnter amount to deposit: "))
                ver_deposit = input("Is this the correct amount, Yes, or No ? " + str(amt) + " ")
                if ver_deposit == "Yes":
                    # Calling deposit method
                    accountObj.deposit(amt)
                    # Printing updated balance
                    print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")
                    print("you have only 3 deposit times remaining")
                else:
                    exit()
            # QUIT
            elif selection == 4:
                check = input("Are you sure you want to quit?, Yes, or No:")
                if check == "Yes":
                    print("\nYour Transaction is complete")
                    print("Transaction number: ", random.randint
                            (10000, 1000000))
                    print("Thanks for choosing us as your bank")
                else:
                    main()
              
 
           # Any other choice
            else:
                print("\nThat's an invalid choice.")
                #break;
# call main
main()