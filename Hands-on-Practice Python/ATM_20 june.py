#ATM
class Account:
    interest=0.5
    def __init__(self,f_name,l_name,acc_no=0,initial_balance=100,trans_id=0):
        self.fname=f_name
        self.lname=l_name
        self.acc_no=acc_no
        self.balance=initial_balance
        self.trans_id=trans_id
    def deposit(self,amount):
        self.balance+=amount
        self.trans_id=self.trans_id+1
    def withdraw(self,amount):
        if(amount>self.balance):
            print("Transaction declined, insufficient balance")
        else:
            self.balance-=amount
            self.trans_id=self.trans_id+1
    def pay_interest(self):
        monthly_rate=self.interest/12
        monthly_sum=monthly_rate*self.balance
        return monthly_sum+self.balance
    def display(self):
        print("Account name=",self.fname+self.lname)
        print("Account number=",self.acc_no)
        print("Account Balance",self.balance)
        if(self.trans_id!=0):
            print("transaction id=",self.trans_id)
        else:
            print("No transaction performed yet")
account1=Account("Riya","Singh")
account1.display()
a=int(input("enter amount to add"))
account1.deposit(a)
account1.display()

    
