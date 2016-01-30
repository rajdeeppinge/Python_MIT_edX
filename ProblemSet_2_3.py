balance = 999999
annualInterestRate = 0.18
bal = balance
lower = balance/12
upper = (balance * (1+annualInterestRate/12.0)**12)/12.0
epsilon = 0.001

def lowest_pay():
    global bal
    for month in range(1,13):
        bal -= lowestPay
        bal = bal + (annualInterestRate/12.0)*bal
        
while abs(bal) > epsilon:
    bal = balance
    lowestPay = (lower + upper)/2.0
    lowest_pay()
    if bal > 0:
        lower = lowestPay
    elif bal < 0:
        upper = lowestPay
    
print "Lowest Payment:", round(lowestPay, 2)