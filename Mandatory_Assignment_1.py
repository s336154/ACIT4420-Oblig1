# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 18:58:53 2024

@author: s336154
"""


##################### Exercise 1 ###########################


def find_prime_factors(n):
    prime_factors = []
    
    #Dividing out all factors of 2 first (handling even numbers)
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    
    #Checking only odd numbers, starting from 3
    i = 3
    while i * i <= n:
        while n % i == 0:
            prime_factors.append(i)
            n //= i
        i += 2  # Skipping even numbers, only testing odd numbers

    # If n is still greater than 1, then it is prime
    if n > 1:
        prime_factors.append(n)

    return prime_factors



print("\n\n\n",find_prime_factors(10))




##################### Exercise 2 ###########################


class BankAccount:
    def __init__(self, account_holder):
        #Initializing account holder and set balance to 0
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        #Depositing a specified amount to the balance
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        #Withdrawing a specified amount if sufficient funds exist
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds or invalid amount.")

    def account_info(self):
        #Returning the account holder's name and current balance
        return f"Account Holder: {self.account_holder}, Balance: {self.balance:.2f}"
    

# Derived class for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, interest_rate=0.02):
        #Initializing account holder and set the interest rate
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        #Applying interest to the current balance
        if self.balance > 0:
            interest = self.balance * self.interest_rate
            self.balance += interest
            print(f"Applied interest of {interest:.2f} to {self.account_holder}'s account.")
        else:
            print("No balance to apply interest on.")

# Derived class for Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, transaction_fee=1.0):
        #Initializing account holder and setting the transaction fee
        super().__init__(account_holder)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        #Withdrawing an amount and charging a transaction fee
        total_withdrawal = amount + self.transaction_fee
        if total_withdrawal <= self.balance:
            self.balance -= total_withdrawal
            print(f"Withdrew {amount} with a transaction fee of {self.transaction_fee:.2f} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds for withdrawal and transaction fee.")

#Example usage
if __name__ == "__main__":
    #Creating a standard bank account
    account1 = BankAccount("Johnny Debb")
    account1.deposit(1000)
    account1.withdraw(500)
    print(account1.account_info())

    #Creating a savings account and apply interest
    savings_account = SavingsAccount("James Smith")
    savings_account.deposit(2000)
    savings_account.apply_interest()
    print(savings_account.account_info())

    #Creating a checking account and make a withdrawal
    checking_account = CheckingAccount("Chris Brown")
    checking_account.deposit(500)
    checking_account.withdraw(100)
    print(checking_account.account_info())



