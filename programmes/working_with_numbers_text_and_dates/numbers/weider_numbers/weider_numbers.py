#Binary, octal and hexadecimal numbers
#if your work requires dealing with base2, base8 and base16 numbers

#python for base2, base8 and base16 numbers
"""
Base2       Binary              0,1                                 ob      bin()
base8       Octal               0,1,2,3,4,5,6,7                     0o      oct()
base16      Hexadecimal         0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F     0x      hex()

"""
x = 255

#convert decimal to other number systems
print(bin(x))
print(oct(x))
print(hex(x))

#show the number in decimal number  (no conversion required)
print(0b11111111)
print(0o377)
print(0xff)
