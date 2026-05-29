#ATM Withdrawal

balance = int(input("enter the balance :"))
amount = int(input("enter the amount :"))

if balance >= amount :
    if  amount % 100 == 0 :
        print("withdrawal sucessfull")
    else :
        print("amount must be bigger than the 100")
else :
        print("insufficient balance ")