#! /usr/bin/env python3

# This python program will print this pattern:
# 1
# 12
# 123
# 1234
# 12345
# Where the number of rows will be asked from the user.

strValue = input("Enter number of lines: ")

try:
	rows = int(strValue)

	for x in range(1, rows+1):
		for y in range (1, x+1):
			print(y,'', end='', sep=' ')
		print()
except ValueError as error:
	print(error)
