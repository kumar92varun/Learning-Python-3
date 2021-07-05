# Program to learn about Integer built-in data type

## Declaring integers
x = 17		# via integer literals

x = int()	# calling the function. Initializes an integer with value 0

x = int('2d', 16)       # creating an integer from a string value "2d" which has a base of 16 (hexadecimal base)
print(x)

x = int('0b101101', 2)       # creating an integer from a string value "2d" which has a base of 16 (hexadecimal base)
print(x)


## Converting integers into value of a different base
x = bin(45)     # creates a string object that stores binary representation of integer 45
print(x)        # 0b101101

x = hex(45)     # creates a string object that stores hexadecimal representation of integer 45
print(x)        # 0x2d

x = oct(45)     # creates a string object that stores octal representation of integer 45
print(x)        # 0o55



## Some good helper functions
res = 45/4          # Returns the value as a float
print(res)
print(type(res))


res = 45//4         # Returns the value as an int
print(res)
print(type(res))


res = 2**5
print(res)
print(type(res))


res = divmod(45, 4)
print(res)
print(type(res))


res = abs(45)
print(res)
res = abs(-45)
print(res)


x = 45
res = -x
print(res)


x = -45
res = -x
print(res)