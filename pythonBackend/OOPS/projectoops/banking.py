from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):

    @abstractmethod
    def CreateAccount():
        return 0

    @abstractmethod
    def AuthenticateUser():
        return 0

    @abstractmethod
    def withdraw():
        return 0

    @abstractmethod
    def displaybalance():
        return 0

    @abstractmethod
    def deposit():
        return 0


class SavingsAccount(Account):

    def __init__(self):
        self.savingsAccounts = {}

    def CreateAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 999999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print(self.accountNumber)

    def AuthenticateUser(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print("You are a valid user")
                self.accountNumber == accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication Failure")

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber[1]]:
            print("insufficient balance")
        else:
            self.savingsAccounts[self.accountNumber[1]]-withdrawalAmount
            print("success")
            self.displaybalance()

    def displaybalance(self):
        print(self.savingsAccounts[self.accountNumber][1])

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber] =+ depositAmount
        print("deposit is successfull")
        self.displaybalance()

savingSAccount = SavingsAccount()

while True:
    print(" enter 1 to create a new account")
    print("enter 2 to access an existing account")
    print("enter 3 to exit")
    userchoice = int(input())
    if userchoice is 1:
        print("enter your name :")
        name = input()
        print("enter your deposit:")
        deposit = int(input())
        savingSAccount.CreateAccount(name, deposit)
    elif userchoice is 2:
        print("enter your name :")
        name = input()
        print("enter you number")
        accountNumber = int(input())
        authenticationStatus = savingSAccount.AuthenticateUser(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("enter 2 to deposit")
                print("display balance")
                print(" 4 to previous menu")
                userchoice = int(input())
                if userchoice is 1:
                    print("enter withdrawal amount")
                    withdrawalamount = int(input())
                    savingSAccount.withdraw(withdrawalamount)
                elif userchoice is 2:
                    print("enter an mount to deposit")
                    depositAmount = int(input())
                    savingSAccount.deposit(depositAmount)
                elif userchoice is 3:
                    savingSAccount.displaybalance()
                elif userchoice is 4:
                    break


    elif userchoice is 3:
        quit()
