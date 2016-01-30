balance = 3926
annualInterestRate = 0.2
bal = balance
lowestPay = 0

def lowest_pay():
    global bal
    for month in range(1,13):
        bal -= lowestPay
        bal = bal + (annualInterestRate/12.0)*bal
        
while bal > 0:
    bal = balance
    lowestPay += 10
    lowest_pay()
    
print "Lowest Payment:", lowestPay