
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")

#formatting_percentage numbers
print(f"Sales Tax Rate {sales_tax_rate: .2%}")
print(f"Sales Tax Rate {sales_tax_rate: .1%}")
print(f"Sales Tax Rate {sales_tax_rate: .9%}")

# f-string can be enclosed in single, double or triple quotation marks
sample1 = f'Sales Tax Rate {sales_tax_rate: .2%}'
sample2 = f"Sales Tax Rate {sales_tax_rate: .2%}"
sample3 = f'''Sales Tax Rate {sales_tax_rate: .2%}'''
sample4 = f"""Sales Tax Rate {sales_tax_rate: .2%}"""

#output of formatted strings
print(sample1)
print(sample2)
print(sample3)
print(sample4)