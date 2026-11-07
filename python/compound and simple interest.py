p=int(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=int(input("Enter the time in years: "))
ci=p*(1+r/100)**t
si=p*r*t/100
print("Compound Interest is:", ci)
print("Simple Interest is:", si)
print("thank you for using this program")

