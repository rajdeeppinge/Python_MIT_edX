balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPayment = 0

print "balance =", balance
print "annualInterestRate =", annualInterestRate
print "monthlyPaymentRate =", monthlyPaymentRate

for month in range(1,13):
    print "Month:", month
    monthlyPay = balance * monthlyPaymentRate
    print "Minimum monthly payment:", round(monthlyPay, 2)
    balance -= monthlyPay
    totalPayment += monthlyPay
    balance = balance + (annualInterestRate/12.0)*balance
    print "Remaining balance:", round(balance, 2)
    
print "Total paid:", round(totalPayment, 2)
print "Remaining balance:", round(balance, 2) 