print('Enter Pre-tax Income')
pretaxIncome = input()

print('Enter Base Tax')
baseTax = input()

print('Enter Amount Over Base Bracket')
baseBracket = input()
amountOverBaseBracket = float(pretaxIncome) - float(baseBracket)

print('Your Amount over Base is', amountOverBaseBracket)

print('Enter Marginal Rate in Decimal Form')
marginalRate = input()
marginalRatebyAmountOverBase = float(amountOverBaseBracket) * float(marginalRate)

taxPayable = float(baseTax)+(float(marginalRate)*float(amountOverBaseBracket))

print('Your Tax Payable is', taxPayable)