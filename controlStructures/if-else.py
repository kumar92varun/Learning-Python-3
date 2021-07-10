# Program to learn about conditional branching control structure: IF-ELSE

# Asking an age from the user
while True:
	try:
		ageString = input("Enter an age: ")
		age = int(ageString)
		break
	except:
		print("Invalid input, please re-try")


if age > 20:
	print("Age is greater than 20")
elif age == 15:								# elif are optional; we may omit them if required
	print("Age is exactly 15")
elif age == 16:
	print("Your age is sweet sixteen!")
else:										# final else is also optional; we may omit this
	print("Your age is not special one")


print("\n\n-->If-Else in a single line statement")
name = 'The Varun' if age == 14 else 'Guest'
print(name)


print("\n\n-->Critical use of parenthesis () in single-line If-Else")
ageAfter20Years = age + (0 if age == 14 else 20)
print(name, "'s current age is ", age, " years. After 20 years, ", name, " will be ", ageAfter20Years, " years old.", sep="")