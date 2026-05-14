balance = 0

def deposit():
    global balance
    amt = float(input("Deposit: "))
    balance += amt

def withdraw():
    global balance
    amt = float(input("Withdraw: "))
    if amt <= balance:
        balance -= amt
    else:
        print("Insufficient balance")

while True:
    print("\n1.Deposit 2.Withdraw 3.Check 4.Exit")
    ch = input("Choice: ")
    
    if ch == '1':
        deposit()
    elif ch == '2':
        withdraw()
    elif ch == '3':
        print("Balance:", balance)
    else:
        break
