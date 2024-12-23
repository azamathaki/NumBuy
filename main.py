
from entity.Number import Number
from entity.User import User
from entity.Bank import Bank

# creating bank account and balance
myBalance = 60
myAccount = Bank(myBalance)

# creating user
john = User("John Doe")

# and number for user
phone_number = Number(john,"+998909001123")


def run(user,number,account):
    """ here we can check process and do operations. Thing that i like about this
    is that if any failure happens registeration will be set to None which means provides strong security and it
    prevents from any kind of data lose or data corruption. """

    # get balance before running
    print("Your balance before process: ", account.get_balance(),"$")

    # try to buy a number
    print(number.buy(account))

    # get balance after process
    print("Your balance after process: ", account.get_balance(),"$")

    # check user (we have to get error on porpose if we have no money to buy number because all user setting will be set 'None')
    print(number.get_owner())


run(john,phone_number,myAccount)





