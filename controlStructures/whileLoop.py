# Program to learn about while loops
counter = 0

while counter < 101:
	if counter % 5 == 0:
		print("Multiple of 5, continue...")
		counter += 1
		continue		# If a continue statement is occurred, control will immediately go to the starting of the loop
	elif counter == 97:
		print("Faced 97, breaking the loop...")
		break
	else:
		print("Counter is: ", counter)
		counter += 1
else:
	print("While loop ended successfully without any unhandled breakage")
