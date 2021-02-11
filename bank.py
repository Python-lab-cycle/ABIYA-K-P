class bank():
    def __init__(self,acnt,nam,typ,amt):
        self.ac=acnt
        self.name=nam
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("Account Name",self.name)
        print("Account Number=",self.ac)
        print("Account Type=",self.type)
        print("bal=",self.amount)
    def with1(self,w1):
        return(self.amount-w1)
n=input("Enter Name ")
t=input("Enter Type")
a=int(input("Enter Number:"))
am=int(input("Enter Amount:"))
obj=bank(a,n,t,am)
print("Account Details")
obj.printamt()
w=int(input("Enter amount to withdraw"))
print("b1=",obj.with1(w))
#print()
    
