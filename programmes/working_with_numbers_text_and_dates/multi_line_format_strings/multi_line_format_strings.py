# Making multi_line format strings
user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
print(f"{user1} \n{user2} \n{user3}")

#Example2
#using tripple quotation marks (single or double)
unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
sub_total = quantity * unit_price
sales_tax = sub_total * sales_tax_rate
total = sub_total + sales_tax
output = f"""
Subtotal: ${sub_total:,.2f}
Sales Tax: ${sales_tax:,.2f}
Total: ${total:,.2f}

"""
print(output)