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


# Creating dictionaries using empty braces
d2 = {'id':45, 'year':1947, 'age':14, 'oldDictionary':d1}
print(d2)


# Creating dictionaries using Dictionary.fromkeys() method
keySequence = ('key1', 'key2', 'key3', 'key4', 'key5')
defaultValue = 'Varun'
valueSequence = ('value1', 'value2', 'value3', 'value4', 'value5')
d1 = dict.fromkeys(keySequence)		# Will initialize the dictionary with all values set to None
print(d1)

d2 = dict.fromkeys(keySequence, defaultValue)
print(d2)

d3 = dict.fromkeys(keySequence, valueSequence)		# WIll initialize all the keys with each value as tuple valueSequence
print(d3)


print('-> Accessing dictionary elements')
print(d2['id'])


print("-> Trying to access a dictionary element whose key don't exists")
try:
	print(d2[0])
except KeyError:
	print('Trying to access a non-existing key will raise a KeyError exception')


print('-> Deleting dictionary elements')
print(d2)
del d2['oldDictionary']
print(d2)


# Iterating dictionary items
print("-> Iterating dictionary elements")

d1 = {'id':45, 'year':1947, 'age':14, 'first_name':'Varun', 'last_name':'Kumar', 'hobbies':['Programming', 'Cloud', 'Cloud solutions']}

print("--> Iterating dictionary elements - (key,value) pairs - the tuple way")
for item in d1.items():
	print("Item: ", item, type(item))		# In this form the item is a tuple with two items in it. 1st item is key, 2nd item is value
	print("Key: ", item[0])
	print("Value: ", item[1])
	print()

print("--> Iterating dictionary elements - (key,value) pairs - unpacked tuple way")
for (key, value) in d1.items():		# Here we are unpacking the tuple into two values: key and value
	print("Key: ", key)
	print("Value: ", value)
	print()

print("--> Iterating dictionary elements - keys only using dictionary.keys() method")
for key in d1.keys():
	print(key)

print("--> Iterating dictionary elements - keys only")
for key in d1:		# Here the dictionary is treated as an iterable that iterates over its keys
	print(key)

print("--> Iterating dictionary elements - values only")
for value in d1.values():
	print(value)

# Understanding Dictionary Views
print("\n\n--> Dictionary Views")
"""
Dictionary.items(), Dictionary.keys() and Dictionary.values() all returns a Dictionary View.

Dictionary Views are read-only iterable objects that are one-way binded with the original dictionary (i.e. if dictionary mutates, automatically the dictionary view will update).
"""

itemView = d1.items()		# WIll return a 'dict_items' dictionary view
print(itemView)
print(type(itemView))		# Data type: 'dict_items'
d1['favourite_subject'] = 'Astronomy'
print(itemView)		# We didn't updated this Dictionary view, but it is automatically updated as we mutated the source dictionary


print('\n')
keyView = d1.keys()		# WIll return a 'dict_keys' dictionary view
print(keyView)
print(type(keyView))		# Data type: 'dict_keys'
d1['another_favourite_subject'] = 'Sleeping'
print(keyView)		# We didn't updated this Dictionary view, but it is automatically updated as we mutated the source dictionary


print('\n')
valueView = d1.values()		# WIll return a 'dict_values' dictionary view
print(valueView)
print(type(valueView))		# Data type: 'dict_values'
d1['favourite_subject'] = 'More Astronomy'
d1['another_favourite_subject'] = 'More Sleeping'
print(valueView)		# We didn't updated this Dictionary view, but it is automatically updated as we mutated the source dictionary


# Using membership operators ('in' and 'not in') with DIctionaries
print("\n\n--> Using Membership Operators 'in' and 'not in'")
d1 = {
	'id': 45,
	'year': 1947,
	'age': 14,
	'first_name': 'Varun',
	'last_name': 'Kumar',
	'hobbies': ['Programming', 'Cloud', 'Cloud solutions'],
	'subjects': {
		'maths': 'Good',
		'science': 'Superb',
		'physics': 'The best',
	}
}
print('age' in d1)		# Membership operators will check for Keys (NOT VALUES)
print('subjects' not in d1)
print('laptops' not in d1)
print('subjects.science' in d1)		# Checking for nested keys isn't possible in this way


# Using some common important Dictionary Methods
print("\n\n--> Using some important Dictionary methods")
d1 = {
	'id': 45,
	'year': 1947,
	'age': 14,
	'first_name': 'Varun',
	'last_name': 'Kumar',
	'hobbies': ['Programming', 'Cloud', 'Cloud solutions'],
	'subjects': {
		'maths': 'Good',
		'science': 'Superb',
		'physics': 'The best',
	}
}
print("\n----> Shalow copying a dictionary")
d2 = d1.copy()		# Returns a shalow copy of d1
print(d2)
d1['id'] = 45000000
print(d2)
print(d1)

print("\n----> Using Dictionary.get(key)")
d1 = dict(id=45, rollnumber=6183270, name='Varun')
print(d1.get('id'))		# If key exists; will return the value of that key
print(d1.get('age'))	# If key don't exist; will return None

print("\n----> Using Dictionary.get(key, fallBack)")
d1 = dict(id=45, rollnumber=6183270, name='Varun')
print(d1.get('id', 'fallbackid'))		# If key exists; will return the value of that key
print(d1.get('age', 'fallbackage'))  # If key don't exist; will return the passed fallback value (2nd argument)

print("\n----> Using Dictionary.setdefault(key, value)")
d1 = dict(id=45, rollnumber=6183270, name='Varun')
print(d1.setdefault('id', 99999))		# If key exists; will return the value of that key
print(d1.get('id'))						# Returns the same value as above (45), the 2nd argument (99999) wasn't updated
print(d1.setdefault('age', 14))			# For keys that don't exists, 'age', setdefault will create a new key and assign the given value to it
print(d1.get('age'))					# Due to Dictionary.setdefault(), now this is a valid key

print("\n----> Using Dictionary.update(another dictionary / List of list elements / List of tuple elements / Tuple of list elements / Tuple of tuple elements)")
d1 = dict(name='Varun', age=14)
print(d1)

print("\n------> Updating a dictionary via another dictionary")
d2 = {
	'name': 'Varun Kumar',
	'age': 14,
	'roll_number': 6183270,
	'hobbies': ['Astronomy', 'Physics']
}
d1.update(d2)		# A dictionary can be updated via another dictionary
print(d1)

print("\n------> Updating a dictionary via a list of tuple elements")
l1 = [('name', 'Coming from tuple'), ('age', 99), ('subjects', ['Arts', 'Science'])]
d1.update(l1)		# A dictionary can also be updated via a list, containing tuple elements containing exactly 2 elements, if more or less elements given in tuple, will throw a ValueError exception
print(d1)

print("\n------> Updating a dictionary via a tuple of tuple elements")
t1 = (('favouriteColor', 'Blue'), ('favouriteFood', 'Indian'), ('age', 16), ('carBrand', 'Audi'))
d1.update(t1)		# A dictionary can also be updated via a tuple, containing tuple elements containing exactly 2 elements, if more or less elements given in tuple, will throw a ValueError exception
print(d1)

print("\n------> Updating a dictionary via a list of list elements")
l2 = [['name', 'Tony Stark'], ['company', 'Stark Industries'], ['age', 'Around 50s'], ['carBrand', 'He also uses Audi']]
d1.update(l2)
print(d1)


print("\n----> Using Dictionary.pop(key)")
d1 = dict(name='Varun', age=14, surname='Kumar')
print(d1.pop('name'))
print(d1)
try:
	print(d1.pop('your name'))
except KeyError:
	print("Popping a non-existent key will raise a KeyError exception")
print(d1)


print("\n----> Using Dictionary.pop(key, fallbackValue)")
d1 = dict(name='Varun', age=14, surname='Kumar')
print(d1.pop('name'))
print(d1)
print(d1.pop('your name', "We didn't had this key so this is the fallback value"))
print(d1)


print("\n----> Using Dictionary.popitem()")
d1 = {
	'name': 'Varun',
	'age': 14,
	'surname': 'Kumar',
	'rollnumber': 6183270
}
for x in range(len(d1)):
	print(d1.popitem())
else:
	print('It appears like popitem will pop the items in the reverse sequence of how they were added in the dictionary (LIFO)')
print(d1)


print("\n----> Clearing a dictionary")
print(d1)
d1.clear()		# WIll clear the whole dictionary
print(d1)
