user_information = {
    "Name": "Sriya",
    "Mobile Number": "",
    "ATM Pin": "3456",
    "Balance": 10000,
    "Transaction History": []
}

print("Please enter your ATM Card:")

remaining_attempts = 3

while remaining_attempts > 0:

    pin = input("Enter 4 digits pin: ")

    if pin == user_information["ATM Pin"]:
        print("Login Successful")

        # Homepage Loop
        while True:

            user_selection = int(input(
                "\nEnter\n"
                "1.Deposit Money\n"
                "2.Withdraw Money\n"
                "3.Pin Change\n"
                "4.Check Balance\n"
                "5.Mini Statement\n"
                "6.Exit\n"
            ))

            # Deposit
            if user_selection == 1:

                deposit_money = int(input("Enter the amount to be deposited: "))

                if deposit_money >= 1000:

                    if deposit_money % 100 == 0:

                        user_information["Balance"] += deposit_money

                        user_information["Transaction History"].append(
                            f"Deposit : {deposit_money}"
                        )

                        print(
                            f"Amount Deposited Successfully\nCurrent Balance : {user_information['Balance']}"
                        )

                    else:
                        print("Enter amount in multiples of 100")

                else:
                    print("Minimum deposit should be 1000 or above")

            # Withdraw
            elif user_selection == 2:

                withdraw_money = int(input("Enter the amount to be withdrawn: "))

                if withdraw_money <= user_information["Balance"]:

                    if withdraw_money % 100 == 0:

                        user_information["Balance"] -= withdraw_money

                        user_information["Transaction History"].append(
                            f"Withdraw : {withdraw_money}"
                        )

                        print(
                            f"Withdrawal Successful\nCurrent Balance : {user_information['Balance']}"
                        )

                    else:
                        print("Enter amount in multiples of 100")

                else:
                    print("Insufficient Balance")

            # PIN Change
            elif user_selection == 3:

                new_pin = input("Enter new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():

                    user_information["ATM Pin"] = new_pin

                    print("PIN changed successfully")

                else:
                    print("Invalid PIN format. Enter exactly 4 digits")

            # Check Balance
            elif user_selection == 4:

                print(
                    f"Your Current Balance is : {user_information['Balance']}"
                )

            # Mini Statement
            elif user_selection == 5:

                print("------ Transaction History ------")

                if len(user_information["Transaction History"]) == 0:
                    print("No transactions made")

                else:
                    for transaction in user_information["Transaction History"]:
                        print(transaction)

            # Exit
            elif user_selection == 6:

                print("Thank You")
                break

            else:
                print("Invalid Selection")

        break

    else:

        remaining_attempts -= 1

        if remaining_attempts > 0:
            print(f"Wrong PIN! Remaining Attempts: {remaining_attempts}")

        else:
            print("Your card has been blocked")
