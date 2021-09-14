# Program to learn about exception handling

'''
Raising exceptions indicate one (or both) out of two things:
1. an error has occurred
2. a suitable condition has been met, need to pass control out of the current suite

Structure of a try-catch block:

try:
	trySuite
except Exception1:
	exception1Suite
except Exception2:
	exception2Suite
except ExceptionX:
	exceptionXSuite
else:
	elseSuite
finally:
	finallySuite
'''

run = True
while run:
	decision = input("Do you want to continue running this program? (y/n): ")
	try:
		decision = str(decision)
		if decision == 'y':
			exceptionType = input("""Select what type of exception you want to throw?
- IndexError (1)
- KeyError (2)
- ValueError (3)
- EOFError (4)
- EnvironmentError (5)
- ArithmeticError (6)
- ZeroDivisionError (7): """)

			if exceptionType == '1':
				try:
					l1 = ['a', 'b', 'c']
					print(l1[7])
				except IndexError as err:
					print("Caught an IndexError.", err)

			elif exceptionType == '2':
				try:
					d1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
					print(d1['k7'])
				except KeyError as err:
					print("Caught a KeyError.", err)

			elif exceptionType == '3':
				try:
					l1 = ['a', 'b', 'c', 'd']
					(one, two, three) = l1			# Unpacking a list into tuple of values
				except ValueError as err:
					print("Caught a ValueError.", err)

			elif exceptionType == '4' or exceptionType == '5':
				print("Don't have an example of EOFError / EnvironmentError currently")

			elif exceptionType == '6':
				try:
					z = 15 / 0
				except ArithmeticError as err:
					print("Caught an ArithmeticError.", err)

			elif exceptionType == '7':
				try:
					z = 15 / 0
				except ZeroDivisionError as err:
					print("Caught an ZeroDivisionError.", err)

		elif decision == 'n':
			run = False
	except:
		print("Could not parse your input as a string")
else:		# Executes when the while loop has exited safely without any exception / break / return / any other error
	print("Program ended")
