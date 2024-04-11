# from fastapi import FastAPI
#
# app = FastAPI()


def checkAmount(phoneNumber):
    amount = input("Enter amount you want to buy: ")
    if len(amount) > 0 and amount.isnumeric():
        amount = float(amount)
        print(f"Your phone number {phoneNumber} has been credited with ${amount} airtime.")
    else:
        print("Invalid amount. \nTry again.")
        checkAmount(phoneNumber)


def buyAirtime():
    phoneNumber = input("Enter phone number: ")
    if len(phoneNumber) == 10 and phoneNumber.isnumeric():
        checkAmount(phoneNumber)
    else:
        print("Invalid phone number. \nTry again.")
        buyAirtime()


def fundsTransfer():
    bankName = input("Enter bank name: ")
    accountNumber = input("Enter account number: ")
    if len(accountNumber) > 8 and accountNumber.isnumeric():
        amount = input("Enter amount you want to transfer: ")
        print(f"Funds transfer of ${amount} has be initiated to account number {bankName} {accountNumber}")
    else:
        print("Invalid account number. \nTry again.")
        fundsTransfer()


def transactionEntry():
    transactionCode = input(
        "1: Check Balance\n"
        "2: Buy Airtime\n"
        "3: Funds Transfer\n"
        "Select Transaction: "
    )

    if transactionCode == '1':
        print("Your balance is $100.50")
    elif transactionCode == '2':
        buyAirtime()
    elif transactionCode == '3':
        fundsTransfer()
    else:
        print("Invalid entry. \nTry again.")
        transactionEntry()


def confirmUSSD():
    ussd = input("Enter USSD code: ")

    if ussd == "*123#":
        print("Welcome EDWIN MANZONGO")
        transactionEntry()
    else:
        print("Invalid USSD code. \nTry again.")
        confirmUSSD()


confirmUSSD()
# Entry Point
# @app.get("/")
# def root():
#     confirmUSSD()
