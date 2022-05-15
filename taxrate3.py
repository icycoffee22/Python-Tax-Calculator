# GIVEN VARIABLES

baseTax = [0, 
    7500, 
    13750, 
    22250, 
    113900, 
    3400000, 
    5150000, 
    6416667]
margRate = [.15, 
    .25, 
    .34, 
    .39, 
    .34, 
    .35, 
    .38, 
    .35]
baseCap = [0, 
    50000,
    75000,
    100000,
    335000,
    10000000,
    15000000,
    18333333]

# Get Taxable Income and use it to amouOver(income-baseCap)

print('Please enter your income')
income = float(input())

if income <= 50000:
    taxPayable = baseTax[0] + (margRate[0] * (income - baseCap[0]))
    print('Tax Payable is', taxPayable)
elif income >= 50001 and income <= 75000:
    taxPayable = baseTax[1] + (margRate[1] * (income - baseCap[1]))
    print('Tax Payable is', taxPayable)
elif income >= 75001 and income <= 100000:
    taxPayable = baseTax[2] + (margRate[2] * (income - baseCap[2]))
    print('Tax Payable is', taxPayable)
elif income >= 100001 and income <= 335000:
    taxPayable = baseTax[3] + (margRate[3] * (income - baseCap[3]))
    print('Tax Payable is', taxPayable)
elif income >= 335001 and income <= 10000000:
    taxPayable = baseTax[4] + (margRate[4] * (income - baseCap[4]))
    print('Tax Payable is', taxPayable)
elif income >= 10000001 and income <= 15000000:
    taxPayable = baseTax[5] + (margRate[5] * (income - baseCap[5]))
    print('Tax Payable is', taxPayable)
elif income >= 15000001 and income <= 18333333:
    taxPayable = baseTax[6] + (margRate[6] * (income - baseCap[6]))
    print('Tax Payable is', taxPayable)
elif income >= 18333334:
    taxPayable = baseTax[7] + (margRate[7] * (income - baseCap[7]))
    print('Tax Payable is', taxPayable)

input("Press any Key to close")