balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    mir = annualInterestRate / 12.0
    mmp = monthlyPaymentRate * balance
    mub = balance - mmp
    balance = (1 + mir) * mub

print("Remaining balance: {}".format(round(balance, 2)))