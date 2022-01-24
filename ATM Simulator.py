# This is a mini project that simulates an ATM

chances = 0
balance = 15000  # Assume that the user has 15000 naira in their account
account_type = 'Savings'

# To generate a PIN for this account
import random

def generatePIN():
    for i in range(4):
        # randint generates a random number between 0,9
        random.seed(3)
        PIN = ''.join(str(random.randint(0, 9)) for _ in range(4))
    return PIN

stored_pin = generatePIN()

print("----------------------------------------------------------------------------")
print("|                                                                          |")
print("|                   Welcome to Guaranty Trust Bank                         |")
print("|                                                                          |")
print("----------------------------------------------------------------------------")

while chances < 3:
    pin = int(input("Please enter your 4- digit PIN"))

    if pin == int(stored_pin):
        print('''Welcome, choose from the following options:
                Press 1 to Check Balance
                Press 2 for Withdrawal
                Press 3 for Deposit
                Press 4 for Recharge''')

        option = int(input('Choose an option: '))
        if option == 1:
            print('Your current balance is ', balance)
            print('''Would you like to perform another transaction?
                    Press 1 for Yes
                    Press 2 for No''')
            return_option = int(input("Please select an option "))
            if return_option == 1:
                print('''Which transaction will you like to perform?:
                                Press 1 to Check Balance
                                Press 2 for Withdrawal
                                Press 3 for Deposit
                                Press 4 for Recharge''')
            else:
                print("Thank you for choosing Guaranty Trust Bank!")
                break

        elif option == 2:
            withdrawal_amount = int(input('Enter the amount to withdraw: '))
            if withdrawal_amount < balance:
                print('Please take your cash')
                print('''Would you like to perform another transaction?
                        Press 1 for Yes
                        Press 2 for No''')
            else:
                print('Insufficient Funds')
                return_option = int(input())
                if return_option == 1:
                    print('''Which transaction will you like to perform?:
                                                Press 1 to Check Balance
                                                Press 2 for Withdrawal
                                                Press 3 for Deposit
                                                Press 4 for Recharge''')
                else:
                    print("Thank you for choosing Guaranty Trust Bank!")
                    break

        elif option == 3:
            deposit_amount = int(input('Enter the amount to deposit: '))
            print('Transaction completed')
            print("Your new balance is ", deposit_amount + balance)
            print('''Would you like to perform another transaction?
                        Press 1 for Yes
                        Press 2 for No''')
            return_option = int(input())
            if return_option == 1:
                print('''Which transaction will you like to perform?:
                                                            Press 1 to Check Balance
                                                            Press 2 for Withdrawal
                                                            Press 3 for Deposit
                                                            Press 4 for Recharge''')
            else:
                print("Thank you for choosing Guaranty Trust Bank!")
                break

        elif option == 4:

            print('''Choose a network provider

                    1. MTN
                    2. GLO
                    3. AIRTEL
                    4. 9MOBILE''')

            network_provider = int(input('Enter a network provider: '))
            if network_provider == 1 or 2 or 3 or 4:
                number = input('Enter the phone number to recharge: ')
                if len(number) == 11:
                    print('Transaction completed')
                else:
                    print("Please provide a valid phone number")
                print('''Would you like to perform another transaction?
                            Press 1 for Yes
                            Press 2 for No''')

                return_option = int(input())
                if return_option == 1:
                    print('''Which transaction will you like to perform?:
                                                                            Press 1 to Check Balance
                                                                            Press 2 for Withdrawal
                                                                            Press 3 for Deposit
                                                                            Press 4 for Recharge''')
                else:
                    print("Thank you for choosing Guaranty Trust Bank!")
                    break

        else:
            print('You have not selected any option')

    else:
        print('Incorrect PIN entered')

    chances += 1
else:
    print('No more chances. Please take your card')
