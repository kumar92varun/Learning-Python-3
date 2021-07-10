# Program to learn about for loops

print("-->Looping values of an iterable variable")
countries = ['India', 'United States', 'New Zealand']
for country in countries:
	print(country)
else:				# Elso is optional, will be executed when the for loop executes successfully
	print("Printed all the countries list successfully")

print("\n\n-->Looping both key and value of an iterable variable")
countries = ['India', 'United States', 'New Zealand']
numOfCountries = len(countries)
for i in range(numOfCountries):
	print(i)
	print(countries[i])


print("\n\n-->Looping a dictionary items")
abouttMe = {
	'name':'Varun Kumar',
	'age':14,
	'favouriteColor':'blue'
}
for (key, value) in abouttMe.items():
	print(key)
	print(value)


print("\n\n-->Looping a range of numbers between start and stop, and also have an jump offset")
for x in range(1, 100, 3):
	print(x)