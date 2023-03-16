class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + " " + last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)


userList = []


def generateusers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8]), line[9])


def finduser():
    name = input("Enter user's name: ")
    found = False
    for user in userList:
        if name.lower() in user.full_name.lower():
            print("Name:", user.first_name, user.last_name)
            print("Gender:", user.gender)
            print("Address:", user.street_address, user.city)
            print("Email:", user.email)
            print("Credit card number:", user.cc_number)
            print("Credit card type:", user.cc_type)
            print(f"Balance: ${user.balance:.2f}")
            print("Account number:", user.account_no)
            found = True
    if not found:
        print("No users found with that name.")


def overdrafts():
    total_debt = 0
    num_overdrafts = 0
    for user in userList:
        if user.balance < 0:
            print(user.first_name, user.last_name)
            total_debt += user.balance
            num_overdrafts += 1
    print("Total number of users with negative balances:", num_overdrafts)
    print(f"Total debt owed by users: ${total_debt:.2f}")


def missingemails():
    num_missing = 0
    for user in userList:
        if user.email == "":
            print(user.first_name, user.last_name)
            num_missing += 1
    print("Total number of users with missing emails:", num_missing)


def bankdetails():
    total_balance = 0
    highest_balance = float("-inf")
    lowest_balance = float("inf")
    highest_balance_user = None
    lowest_balance_user = None
    for user in userList:
        total_balance += user.balance
        if user.balance > highest_balance:
            highest_balance = user.balance
            highest_balance_user = user
        if user.balance < lowest_balance:
            lowest_balance = user.balance
            lowest_balance_user = user
    print("Total number of users:", len(userList))
    print(f"Bank total worth: ${total_balance:.2f}")
    print(f"User with highest balance:, {highest_balance_user.first_name} "
          f"{highest_balance_user.last_name}, with balance"
          f" ${highest_balance:.2f}")
    print(f"User with lowest balance:, {lowest_balance_user.first_name} "
          f"{lowest_balance_user.last_name}, with balance"
          f" ${lowest_balance:.2f}")


def transfer():
    account_no = input("Enter account number to transfer from: ")
    found_user = False
    for user in userList:
        if user.account_no == account_no:
            print(f"User found: {user.first_name} {user.last_name} ("
                  f"{user.account_no}), Balance: ${user.balance:.2f}")
            found_user = True
            break
    if not found_user:
        print("No user found with the provided account number.")
        return

    transfer_amount = input("Enter amount to transfer: ")
    try:
        transfer_amount = float(transfer_amount)
    except ValueError:
        print("Invalid amount")
        return
    if transfer_amount <= 0 or transfer_amount > user.balance:
        print("Invalid amount.")
        return

    transfer_account_no = input("Enter account number to transfer to: ")
    found_transfer_user = False
    for transfer_user in userList:
        if transfer_user.account_no == transfer_account_no:
            print(f"User to transfer to: {transfer_user.first_name} "
                  f"{transfer_user.last_name} ({transfer_user.account_no}), "
                  f"Balance: ${transfer_user.balance:.2f}")
            found_transfer_user = True
            break
    if not found_transfer_user:
        print("No user found with the provided account number.")
        return

    user.balance -= transfer_amount
    transfer_user.balance += transfer_amount
    print(f"Transfer successful. {user.first_name} {user.last_name} ("
          f"{user.account_no}) new balance: ${user.balance:.2f}, "
          f"{transfer_user.first_name} {transfer_user.last_name} ("
          f"{transfer_user.account_no}) new balance:"
          f" ${transfer_user.balance:.2f}")


userChoice = ""
print("Welcome")
generateusers()
while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()

    if userChoice == "1":
        finduser()
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingemails()
    elif userChoice == "4":
        bankdetails()
    elif userChoice == "5":
        transfer()
    print()
