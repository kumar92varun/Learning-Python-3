# This program will print this pattern:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
import math

while True:
	try:
		strValue = input("Enter the width of the diamond (an odd number): ")
		width = int(strValue)
		modulus = width % 2
		if modulus != 0:
			break
		else:
			print("You entered an even number.")
	except ValueError as err:
		print("You entered a non-numeric value.")
		continue


halfWidth = math.ceil(width/2)

for x in range(1, width+1):
	if x < halfWidth:
		spaceHalf = halfWidth - x
		stars = x*2 - 1
	
	if x == halfWidth:
		spaceHalf = 0
		stars = width

	if x > halfWidth:
		spaceHalf = x - halfWidth
		stars = (width - x)*2 + 1

	# Now printing the pattern:
	for y in range(spaceHalf):
		print(' ', end='')
	
	for y in range(stars):
		print('*', end='')

	for y in range(spaceHalf):
		print(' ', end='')
	print()
print("Program finished.")