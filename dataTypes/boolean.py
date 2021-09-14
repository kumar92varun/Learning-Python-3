# Program to learn about Boolean built-in data type

value = True
print(value)

value = False
print(value)

value = bool()
print(value)			# Passing no argument will give a False

value = bool('')
print(value)			# Empty string will give a False

value = bool(None)
print(value)			# None will give a False

value = bool('12')
print(value)			# Will be True

value = bool(2+2)
print(value)

value = bool(2-2)
print(value)

value = bool(-2)
print(value)

value = bool(0)
print(value)

value = bool(-0)
print(value)
