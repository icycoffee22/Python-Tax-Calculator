print('Please enter Income')
income = input()

if float(income) <= 50000:
    baseTax = 0
    margRate = .15
    baseCap = 0
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)
elif float(income) >= 50001 and float(income) <=75000:
    baseTax = 7500
    margRate = .25
    baseCap = 50000
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)
elif float(income) >= 75001 and float(income) <=100000:
    baseTax = 13750
    margRate = .34
    baseCap = 75000
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)
elif float(income) >= 100001 and float(income) <=335000:
    baseTax = 22250
    margRate = .39
    baseCap = 100000
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)
elif float(income) >= 335001 and float(income) <=10000000:
    baseTax = 113900
    margRate = .34
    baseCap = 335000
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)
elif float(income) >= 10000001 and float(income) <=15000000:
    baseTax = 3400000
    margRate = .35
    baseCap = 10000000
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)
elif float(income) >= 15000001 and float(income) <=18333333:
    baseTax = 5150000
    margRate = .38
    baseCap = 15000000
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)
elif float(income) >= 18333334:
    baseTax = 6416667
    margRate = .35
    baseCap = 18333333
    amouOver = float(income) - float(baseCap)
    taxPayable = baseTax+(margRate*amouOver)
    print("Your payable tax is", taxPayable)

input('Press ENTER to exit')