# Program to learn about Float built-in data type

x = 2.1428
print(x)

x = float(55)
print(x)

x = float('8.9e4')
print(x)

try:
	stringVal = 'ssss'
	x = float(stringVal)
	print(x)
except ValueError as err:
	print("Cannot convert the given string '" + stringVal + "' into float")

# Some important functions related to float
x = 45.5
y = round(x)		# Will round this float to nearest possible integer
z = int(x)			# Will throw away the fractional part and return the integer part
print((y, z))

print((45.6).is_integer())
print((45.0).is_integer())

print(type((45.6)))		# Still a float
print(type((45.6,)))	# Converted to a tuple now becuase of extra comma in the end

x = 2.5
y = x.as_integer_ratio()
print(type(y), y, sep=' => ')

print("============================================")

# Now importing sys module... to print the information provided in sys.float_info
import sys
print(sys.float_info)
print("Max number:", sys.float_info.max)
print("Min number:", sys.float_info.min)

print("Max exponential:", sys.float_info.max_exp)
print("Min exponential:", sys.float_info.min_exp)

print("Max 10 exponential:", sys.float_info.max_10_exp)
print("Min 10 exponential:", sys.float_info.min_10_exp)

print("Digit:", sys.float_info.dig)
print("Mant Digit:", sys.float_info.mant_dig)

print("Epsilon:", sys.float_info.epsilon)

print("Radix:", sys.float_info.radix)

print("Rounds:", sys.float_info.rounds)

print("============================================")

# Now importing math module and see some good helper functions
import math

x = -3.56
y = math.ceil(x)
z = math.floor(x)
print('Ceil:', y, ': Floor:', z)

print(math.e)
print(math.pi)
print(math.trunc(-3.41))		# Will truncate the floating point, only returns the integer as an integer. Works same as int(x)