# Program to learn about Disctionaries built-in data type
print('-> Creating dictionaries')
d1 = dict()		# Will create an empty dictionary
print(d1)
print(type(d1))

# Creating dictionaries using Sequence Argument
t1 = ('id', 45)
t2 = ('name', 'Varun')
t3 = ('age', 14)
l1 = [t1, t2, t3, ('mobile', 8826039646), ('places', ['Delhi', 'Gurugram', 'Noida']), ('hobbies', ('Coding', 'Programming'))]
d1 = dict(l1)		# Can create a dictionary using a tuple of list as well. First argument will be used as index, second argument will be used as the value
print(d1)


# This will fail
try:
	d1 = dict(['a', 'b', 'c', 'd', 'e'])
except ValueError:
	print("Cannot use the list argument that don't have every element as a tuple of 2 values")


# Creating dictionaries using Keyword Arguments
d2 = dict(id = 45, year = 1947, age = 14, oldDictionary = d1)
print(d2)
print(len(d2))		# Gives the count of keys in the dictionary


# Creating dictionaries using empty braces
d1 = {}
print(d1)
print(len(d1))

d2 = {'id':45, 'year':1947, 'age':14, 'oldDictionary':d1}
print(d2)


print('-> Accessing dictionary elements')
print(d2['id'])

try:
	print(d2[0])
except KeyError:
	print('Trying to access a non-existing key will raise a KeyError exception')


print('-> Deleting dictionary elements')
print(d2)
del d2['oldDictionary']
print(d2)


