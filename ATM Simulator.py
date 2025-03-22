#ATM Simulator
#A file handling application

#by SillyGreyCat


from os import listdir

#errors -->

class InvalidInput(Exception):
    pass

class AccountNotFound(Exception):
    pass

class IncorrectPin(Exception):
    pass

class InsufficientBalance(Exception):
    pass

class WithdrawalLimitExceeded(Exception):
    pass

class DepositCancelled(Exception):
    pass


#function definitions -->

def info(): #displays basic information
    print("\nOperations: ")
    print("Deposit Money   -->  'dep'")
    print("Withdraw Money  -->  'wth'")
    print("Check Balance   -->  'chk'\n")


def showentries(bank): #to show all records in a bank file
    files = listdir("./ATM Files")
    fname = bank + ".txt"
    if (fname not in files):
        raise InvalidInput("\nCannot access records. \nError: invalid bank name")
    else:
        file = open(f"./ATM Files/{fname}", "r")
        rawdata = file.readlines()
        data = []
        for rd in rawdata:
            data.append(rd.split(','))
        print("\nAccess granted.")
        print(f"\nAll records for {bank}:")
        n = 1
        for entry in data:
            print(f"\nRecord {n}:")
            print(f"--> Account Number: {entry[0]}")
            print(f"--> Account Holder: {entry[2]}")
            print(f"--> Branch Code: {entry[1]}")
            print(f"--> Current Balance: {entry[3]}")
            print(f"--> Withdrawal Limit: {entry[4]}")
            print(f"--> PIN: {entry[5]}")
            n += 1


def withdraw(accno, amnt, pin): #to perform withdrawal transaction
    files = listdir("./ATM Files")
    found = 0
    for i in files:
        file = open(f"./ATM Files/{i}", "r")
        rawdata = file.readlines()
        data = []
        for rd in rawdata:
            data.append(rd.split(','))
        for entry in data:
            if (accno == int(entry[0])):
                found = 1
                print(f"\nHello, {entry[2]}!")
                if (amnt <= int(entry[3])):
                    if (amnt <= int(entry[4])):
                        if (pin == int(entry[5])):
                            entry[3] = str(int(entry[3]) - amnt)
                            break
                        else:
                            raise IncorrectPin("\nWithdrawal failed.\nError: incorrect pin")
                    else:
                        raise WithdrawalLimitExceeded("\nWithdrawal failed.\nError: withdrawal limit exceeded")
                else:
                    raise InsufficientBalance("\nWithdrawal failed.\nError: insufficient balance")
        if (found == 1):
            file.close()
            file = open(f"./ATM Files/{i}", "w")
            rawdata = []
            for entry in data:
                rawdata.append(','.join(entry))
            file.writelines(rawdata)
            file.close()
            break
    if (found == 0):
        raise AccountNotFound("\nWithdrawal failed.\nError: invalid account number")


def deposit(accno, amnt): #to perform deposit transaction
    files = listdir("./ATM Files")
    found = 0
    for i in files:
        file = open(f"./ATM Files/{i}", "r")
        rawdata = file.readlines()
        data = []
        for rd in rawdata:
            data.append(rd.split(','))
        for entry in data:
            if (accno == int(entry[0])):
                found = 1
                print(f"\nHello, {entry[2]}!")
                print("To proceed to add {amt} Rs. to your account, enter 'yes'")
                print("If this is not your name, enter 'no'")
                cnf = input(">>> ")
                if (cnf == "yes"):
                    entry[3] = str(int(entry[3]) + amnt)
                elif (cnf == "no"):
                    raise DepositCancelled("\nDeposit cancelled by user")
                else:
                    raise InvalidInput("\nDeposit failed.\nError: confirmation failed")
                break
        if (found == 1):
            file.close()
            file = open(f"./ATM Files/{i}", "w")
            rawdata = []
            for entry in data:
                rawdata.append(','.join(entry))
            file.writelines(rawdata)
            file.close()
            break
    if (found == 0):
        raise AccountNotFound("\nDeposit failed.\nError: invalid account number")


def check(accno, pin): #to show account details
    files = listdir("./ATM Files")
    found = 0
    for i in files:
        file = open(f"./ATM Files/{i}", "r")
        rawdata = file.readlines()
        data = []
        for rd in rawdata:
            data.append(rd.split(','))
        for entry in data:
            if (accno == int(entry[0])):
                found = 1
                print(f"\nHello, {entry[2]}!")
                if (pin == int(entry[5])):
                    print(f"--> Account Number: {entry[0]}")
                    print(f"--> Branch Code: {entry[1]}")
                    print(f"--> Current Balance: {entry[3]}")
                    print(f"--> Withdrawal Limit: {entry[4]}")
                else:
                    raise IncorrectPin("\nFailed to show details. Error: incorrect pin")
                break
        if (found == 1):
            file.close()
            break
    if (found == 0):
        raise AccountNotFound("\nFailed to show details.\nError: invalid account number")


#main -->

loop = 1
adminpass = 25807 #to perform admin operations
oplist = ['help', 'dep', 'wth', 'chk', 'showall', 'sysexit'] #operation list
print("\n~ ~ ~ ~ ~ ~ ~ Welcome to ATM ~ ~ ~ ~ ~ ~ ~")
info()

while (loop == 1): #end loop by typing 'sysexit'
    print("\nEnter operation to perform \nOr 'help' for information")
    opcode = input(">>> ")
    print("")
    try:
        if (opcode not in oplist):
            raise InvalidInput("\nFailed to perform operation.\nError: invalid operation code")

        else:
            #help
            if (opcode == "help"): #displays basic information
                info()

            #normal operations
            elif (opcode == "wth"): #executes 'withdraw'
                print("Enter details:")
                acn = int(input("Account Number: "))
                amt = int(input("Amount: "))
                pn = int(input("PIN: "))
                withdraw(acn, amt, pn)
                print("Amount successfully withdrawn.\n")

            elif (opcode == "dep"): #executes 'deposit'
                print("Enter details:")
                acn = int(input("Account Number: "))
                amt = int(input("Amount: "))
                deposit(acn, amt)
                print("Amount successfully deposited.\n")

            elif (opcode == "chk"): #executes 'check'
                print("Enter details:")
                acn = int(input("Account Number: "))
                pn = int(input("PIN: "))
                check(acn, pn)

            #admin operations (not shown in 'info')
            elif (opcode == "showall"): #executes 'show entries'
                print("Enter details:")
                bank = input("Bank Name: ")
                code = int(input("Admin Password:"))
                if (code != adminpass):
                    raise IncorrectPin("\nCannot display records.\nError: incorrect admin password")
                else:
                    showentries(bank)

            #exit program
            elif (opcode == "sysexit"): #sets loop condition to false
                print("\nExiting system.")
                loop = 0

            else: #space for undeveloped operations
                pass

    #print error message for various errors
    except InvalidInput as error:
        print(error)

    except AccountNotFound as error:
        print(error)

    except IncorrectPin as error:
        print(error)

    except InsufficientBalance as error:
        print(error)

    except WithdrawalLimitExceeded as error:
        print(error)

    except DepositCancelled as error:
        print(error)

    #handles unknown errors. if encountered, fix it.
    except:
        print("Some unknown error occured.")
