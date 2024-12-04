class Bank():
    accno:int
    balance:int
    ac_type:str
    customer_name:str

    def __init__(self,acc_no,balance,acc_type,customer_name):
        self.accn_no=acc_no
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name

    def deposit(self,amount):
        self.balance+=amount
        print(f"your account{self.acno}has been credited with amount{amount}avl bal{self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            self.balance-=amount
            print(f"your account{self.accno}has been debited with amount{amount} avl bal{self.balance}")

    def get_balance(self):
        print(f"your avl  bal",self.balance)

bank_instance1=Bank(121,5000,"permanent","paru")
bank_instance1.deposit(2500)              



     
