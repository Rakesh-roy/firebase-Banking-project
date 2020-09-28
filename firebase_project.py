from firebase.firebase import FirebaseApplication

def connectFirebase():
    fire = FirebaseApplication("https://bank-b46c1.firebaseio.com/", None)
    return fire

def createAccount():
    print("-------Welcome To our Project Bank------- \n\tCreate Your New Account\n")
    acno = int(input("Enter Account No : "))

    fire = connectFirebase()
    result = fire.get("Savings_Account",acno)

    if result:
        print("Sorry Account Already Taken...!!")

    else:
        name = input("Enter Your Name : ")
        pin = int(input("Enter PIN no : "))
        opn_bal = int(input("Enter opening Amount : "))
        data = {"name": name, "pin_no": pin, "balance": opn_bal}
        fire.put("Savings_Account",acno,data)
        print('\n')
        print("Congrats..!! Your Account is Created..!!\n")

def deposit():
    print("Welcome To Deposit\n")
    acno = int(input("Enter Account No : "))

    fire = connectFirebase()
    result = fire.get("Savings_Account",acno)

    if result:
        amount = int(input("Enter Amount to deposit : "))
        total = amount+result["balance"]
        fire.patch("Savings_Account/"+str(acno), {"balance" : total})
        print('\n')
        print("Congrats..!! Your Amount Diposited in Your Account..!!\n")

    else:
        print("Sorry Account No is not Available...!!")


def withdraw():
    print("Welcome To Withdraw\n")
    acno = int(input("Enter Account No : "))

    fire = connectFirebase()
    result = fire.get("Savings_Account",acno)

    if result:
        amount = int(input("Enter Amount to Withdraw : "))
        if amount <= result['balance']:
            total = result["balance"]-amount
            fire.patch("Savings_Account/"+str(acno), {"balance" : total})
            print("You withdrawn Amount :",amount," from Your Account.\n")
        else:
            customer = fire.get("Savings_Account", acno)
            print("Sorry...!!",customer["name"]," you have Insufficient balance in your account")
            print("Available balance : ",customer['balance'])

    else:
        print("Sorry Account No is Invalid...!!")

def viewBalance():
    acno = int(input("Enter Account No to view your balance: "))
    fire = connectFirebase()
    result = fire.get("Savings_Account",acno)
    if result:
       print("Your Balance is : ", +result['balance'],"\n")
    else:
       print("Sorry Account No is not Available...!!\n Thanks")

while True:
    print('------------------------------------------')
    print("********Welcome to Bank Project********")
    print('------------------------------------------')
    print("\t1) Create New Account")
    print("\t2) Deposit")
    print("\t3) Withdraw")
    print("\t4) Check Balance")
    print("\t5) Exit Bank\n")

    opt = int(input("\tEnter Your Option : "))
    print("\n")

    if opt == 1:
        createAccount()

    if opt == 2:
        deposit()

    if opt == 3:
        withdraw()

    if opt == 4:
        viewBalance()

    if opt == 5:
        print("Thanks Visit Again...!!!")
        break
