p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))

amount = p * (1 + r / 100) ** t
ci = amount - p

print("Compound Interest =", ci)
print("Total Amount =", amount)