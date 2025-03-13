annual_gross_salary=float(input("Annual gross salary: "))
annual_net_salary=float(input("Annual net salary: "))
total_tax_payable=float(input("Total tax payable: "))

# Compute Net Salary
annual_net_salary = annual_gross_salary- total_tax_payable

# Display results
print("\n--- Net Salary Details---")
print(f"Annual Gross Salary: ₹{annual_gross_salary:.2f}")
print(f"Total Tax Payable: ₹{total_tax_payable:.2f}")
print(f"Annual Net Salary: ₹{annual_net_salary:.2f}")