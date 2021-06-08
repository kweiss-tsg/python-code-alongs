# define user input
gross_inc = input("Enter your gross income from your W-2 for 2020: ")
num_dep = input("How many dependents are you claiming? ")

# convert the input values to numbers
gross_inc_float = float(gross_inc)
num_dep_int = int(num_dep)

# calculate taxable income
tax_income = gross_inc_float - 12200 - (2000 * num_dep_int)

# calculate tax rate
if tax_income < 0:
    tax_rate = 0
elif tax_income < 9876:
	tax_rate = .10
elif tax_income < 40126:
	tax_rate = .12
elif tax_income < 85526:
	tax_rate = .22
elif tax_income < 163301:
	tax_rate = .24
elif tax_income < 207351:
	tax_rate = .35
else:
	tax_rate = .37

# calculate the tax due
tax_due = tax_income * tax_rate

# report the results to the user
print("Your gross income is $" + gross_inc + ".")
print("You have " + num_dep + " dependents.")
print ("Your taxable income is $" + str(tax_income) + ".")
print ("Your tax rate is %" + str(int(100 * tax_rate)) + ".")
print ("Your tax due is $" + str(tax_due) + ".")