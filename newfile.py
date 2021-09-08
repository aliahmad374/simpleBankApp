class BankAccount :

    def __init__(self):
        self.balance=0
        self.data=[]

    def depositmoney(self):
        amount=float(input("Enter the Amount you want to deposit: "))
        if amount>0:
            self.balance=self.balance+amount
            print("Amount Deposited",amount)
        else:
            print("Amout must me greater than zero")

    def withdrawmoney(self):
        amount=float(input("Enter the Amount you want to withdraw: "))
        if self.balance>amount:
            self.balance=self.balance-amount
            print("Your withdraw amount is :",amount)

        else:
            print("Insufficient balance")


    def checkbalance(self):
        print("Balance = ",self.balance)


    def createAccount(self):
        name=input("Please Enter your name")
        cnic=input("Please Enter your CNIC")
        pin=int(input("Please Enter your PIN"))

        self.data.append({"name":name,"cnic":cnic,"pin":pin})

        print("Congra!! Your Account is Create Please go Back and Log in")

    def login(self):
        flag=False
        cnic=input("Enter your CNIC")
        pin=int(input("Enter your pin"))

        for li in self.data:
            if li['cnic']==cnic and li['pin']:
                flag=True
                break
        if flag==True:
            while (True):
                print("Wellcome to XYZ Bank")
                print("----------------------------")
                print("press 1 to Enter the money you want to deosit")
                print("press 2 to Enter the money you want to WithDraw")
                print("press 3 to Check balance")
                print("press 4 to logout")

                choice = input("Please Enter your choice")
                if choice == '1':
                    account.depositmoney()
                    print("-----------------------------------------------")

                if choice == '2':
                    account.withdrawmoney()
                    print("-----------------------------------------------")

                if choice == '3':
                    account.checkbalance()
                    print("-----------------------------------------------")
                if choice == '4':
                    break;

                else:
                    print("please choose 1 or 2 or 3 or 4 as a choice")

        else:
            print("Incorrect CNIC or PIN")





# create bject

account=BankAccount()





while(True):
    print("press 1 to create a new Account")
    print("press 2 to Log in your Account")
    print("press 3 to exit")

    option=input("Press 1,2 or 3")

    if option=='1':
        account.createAccount()
        print('--------------------------------------------------------------------------------')

    if option=='2':
        account.login()
        print('--------------------------------------------------------------------------------')

    if option=='3':
        break

    else:
        print("Please press 1 ,2 or 3")
        print('--------------------------------------------------------------------------------')







