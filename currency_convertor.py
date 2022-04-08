with open('D:\\Python\\Python Course with Notes\\currency_exchange.txt') as f:
    rates = f.readlines()

currencyDict ={}
for  rate in rates:
    parsed = rate.split('\t')
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter the amount : "))
print('''Enter the Currenncy you want to convert this into
below are the available Options ''')
[print(item) for item in currencyDict.keys()]
currency = input("Enter one of the currencies: \n")
print(f"{amount} INR is Equal to {amount* float(currencyDict[currency])} {currency}")
