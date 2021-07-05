# Program to print the following pattern:
# ----------
# |\      /|
# | \    / |
# |  \  /  |
# |   \/   |
# |   /\   |
# |  /  \  |
# | /    \ |
# |/      \|
# ----------

while True:
	try:
		strValue = input("Enter an even integer: ")
		width = int(strValue)

		modulus = width % 2
		if modulus == 0:
			break
		else:
			print("You entered an odd number.")
	except ValueError:
		print("You entered a non-integer value.")


halfWidth = int(width/2)

for x in range(1, width+1):
	if x == 1 or x == width:
		for y in range(width):
			print('-', end='')
	else:
		print('|', end='')

		if x <= halfWidth:
			spaceCenter = (halfWidth-x)*2
			spaceLeft = int((width - spaceCenter - 4)/2)
			spaceRight = spaceLeft

			for y in range(spaceLeft):
				print(' ', end='')

			print('\\', end='')

			for y in range(spaceCenter):
				print(' ', end='')

			print('/', end='')

			for y in range(spaceRight):
				print(' ', end='')
		
		if x > halfWidth:
			spaceCenter = (x - halfWidth-1)*2
			spaceLeft = int((width - spaceCenter - 4)/2)
			spaceRight = spaceLeft

			for y in range(spaceLeft):
				print(' ', end='')

			print('/', end='')

			for y in range(spaceCenter):
				print(' ', end='')

			print('\\', end='')

			for y in range(spaceRight):
				print(' ', end='')
		
		print('|', end='')
	print()