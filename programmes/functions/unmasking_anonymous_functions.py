#unmasking anonymous functions
"""
python supports the concept of anonymous functions, 
also called lamda functions

            SYNTAX
lambda arguments : expressions

"""

def lowercaseof(anystring):
    """
    converts all strings to lower case
    """
    return anystring.lower()

print(lowercaseof('Zandusky'))
print(lowercaseof('SCHLEEDORP'))

names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lowercaseof)
print(names)

"""
            SYNTAX
lambda parameters : expressions

"""
lambda anystring : anystring.lower()

names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lambda anystring : anystring.lower())
print(names)

#show number in currency format
currency = lambda n : f"${n:,.2f}"

#show number in percentage format
percent = lambda n : f"${n:,.2%}"

#test currency function
print(currency(99))
print(currency(12345678.09876543))

#test percent function
print(percent(0.065))
print(percent(.5))

#show number in currency format
def currency(n):
    return f"${n:,.2f}"

#show number in percent format
def percent(n):
    return f"${n:.2%}"

#Two functions for formatting numbers with a fixed width.
"""
 python left justify or python right justify
 ( .ljust() and .rjust())
"""
def currency(n , w=15):
    '''
    show in currency format, width=15, or width of your choosing
    '''
    s = f"${n:,.2f}"
    return s.rjust(w)

def percent(n, w=15):
    """
    show in percent format, width=15, or width of your choosing
    """
    s = f"{n:.1%}"
    return s.rjust(w)