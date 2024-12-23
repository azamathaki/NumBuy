
from entity.User import User
from entity.Bank import Bank

class Number:
    def __init__(self, owner, phone_number):
        self.owner = owner
        self.phone_number = phone_number
        self.payment_case = 25  #this is manthly paying case idk what's official call.
        self.payment_cases = { 
            25 : "no limit for calls. 10GB for internet.",
            45 : "no limit for calls and telegram. 20GB for internet.",
            90 : "no limit at all."
                                   }
        self.phone_number_is = 'new' # ['new','used']
        self.phone_number_active = False
        self.commission_fee = 5 #$


    def set_payment_case(self, price):
        self.payment_case = price


    def get_payment_case(self):
        return self.payment_case
    
    def display_cases(self):
        cases = ""
        for key, value in self.payment_cases.items():
            cases += f"{key} : {value} | price: {key}$.\n"
        return cases


    def buy(self, myAccount):
        print(self.display_cases())
        try:
            new_price = int(input("Choose one from given cases list: "))
        except ValueError:
            return "Invalid input. Please enter a valid case number."

        if new_price not in self.payment_cases:
            self.start_over()
            return f"this '{new_price}' payment case is not available in the list! Please choose given cases in the list!"
            
        self.set_payment_case(new_price)
        total_cost = self.get_payment_case() + self.commission_fee
        if myAccount.get_balance() < total_cost:
            self.phone_number_active = False
            self.start_over()
            return "You don't have enough money to change payment case. Please deposit some money to your account!"
        else:
            self.phone_number_is = 'used'
            self.phone_number_active = True
            myAccount.withdraw(total_cost)
            
            return (
            f"Payment successful! Withdrawn {total_cost}$ ({self.commission_fee}$ commission fee) from your account.\n"
            f"Payment case successfully changed to {new_price}$ per month. Enjoy your new payment case!"
            )

    def about(self):
        case_details = self.payment_cases[self.get_payment_case()]
        if (self.phone_number_active == True):
            return (f"This phone number '{self.phone_number}' is successfully registered "
                f"to user '{self.owner.name}'.\n"
                f"Payment case: {case_details} and price: {self.get_payment_case()}$ per month.")
        
    
    def start_over(self):
        if self.phone_number_active == False:
            self.owner = None
            self.phone_number = None
            self.phone_number_is = 'new'

    def get_owner(self):
        if self.owner == None:
            return (f"owner - '{self.owner}' ."
                f"phone number - '{self.phone_number}'."
            )
        else:
            return (f"owner - '{self.owner.get_name()}' ."
                    f"phone number - '{self.phone_number}'."
            )
