#when taxable is False, sales_tax is not added to the total
total = 100
sales_tax_rate = 0.065
taxable = False
if taxable:
    print(f"Total: {total:.2f}")
    sales_tax = sales_tax_rate * total
    print(f"Sales_tax: {sales_tax:.2f}")
    total = total + sales_tax
print(f"Total: {total:.2f}")