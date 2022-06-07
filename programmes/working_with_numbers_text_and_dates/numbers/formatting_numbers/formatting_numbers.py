#formatting with f-strings


user_name = "omara patrick"
print(f"hello {user_name}")

username = "Allan"
print(f"hello {username}")

unit_price = 49.99
quantity = 30
print(f"Subtotal: ${unit_price * quantity}")

#showing dollar amounts
print(f"Subtotal: ${unit_price * quantity:,}")

#to get the pennies to show as two digits
print(f"Subtoatal:${unit_price * quantity:,.2f}")
print(f"Subtoatal:${unit_price * quantity:,.3f}")
print(f"Subtoatal:${unit_price * quantity:,.4f}")