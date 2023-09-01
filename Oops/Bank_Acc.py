class Account:
    
   def __init__(self,acc_no,name,balance):
      self.acc_no=acc_no
      self.name=name
      self.balance=balance

   def deposit_money(self,dep_amount):
      self.balance+=dep_amount
      return self.balance
   def withdraw_money(self,withdraw_amount):
      self.balance-=withdraw_amount
      if(self.balance>=1000):
         return self.balance
      return 0
   
if __name__=="__main__":

   acc_no = int(input("Enter A/C No: "))
   name = input("Enter Name Of A/C Holder: ")
   balance = int(input("Balance: "))
   account = Account(acc_no,name,balance)

   dep_or_withdraw=input("d or w")
   if(dep_or_withdraw=='d'):
      dep_amount=int(input())
      print(account.deposit_money(dep_amount))
   else:
      withdraw_amount=int(input())
      withdrawl=account.withdraw_money(withdraw_amount)
      if(withdrawl==0):print("Insufficient Funds")
      else:print(withdrawl)
        