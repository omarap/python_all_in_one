#All dollar amounts right aligned with a width of 9 characters
unit_Price = 49.95
quantity = 32
sales_tax_rate = 0.65
sub_total = quantity * unit_Price
sales_tax = sales_tax_rate * sub_total
total = sub_total + sales_tax
output = f"""
Subtotal: ${sub_total:>9,.2f}
SalesTax: ${sales_tax:>9,.2f}
Total: ${total:>9,.2f}

"""
print(output)

s_subtotal = "$" + f"{sub_total:,.2f}"
print(s_subtotal)

#All the dollar amounts neatly aligned
#numeric values
s_subtotal = "$" + f"{sub_total:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"

output = f"""
SubtotaL: {s_subtotal:>9}
SalesTax: {s_sales_tax:>9}
Total: {s_total:>9}

"""
print(output)