# Program to learn about Lists built-in data type
print('=== Creating lists ===')
x = list()		# Empty list
print(x)

x = []			# Again, an empty list
print(x)

x = ['a', 'b', 'c']
print(x)
print(type(x))

x = [-17.5, "Kilo", 49, 'V', ['ram', 5, 'echo'], 7, True, False, None]
print(x)
print(type(x[-1]))
print(type(x[-2]))
print(x[-5][-1])

# Converting a tuple into a list. Will only convert the top level elements as list items. 3rd element will not be converted as 
# element which is a list in itself. It will be stored as a tuple only
tuple1 = ('Green', 'Red', ('Bright orange', 'Shalow orange'), 'Yellow', 'Blue')
x = list(tuple1)
print(x)


print('=== Using some common operators with list ===')
print('== Using Membership Operator (in, not in) ==')
list1 = ['Science', 'Maths', 'Chemistry', 'Biology', ('Red', 'Green')]
if 'Maths' in list1:
	print('Maths is in the list!')
if 'Geography' not in list1:
	print('Geography is not in the list!')
if 'Bio' in list1:
	print('Bio is in list')
else:
	print('Bio is not in list')
tuple1 = ('Red', 'Green')
if tuple1 in list1:
	print('Tuple is in list')
else:
	print('Tuple is not in list')


print('== Using Concatenation Operator (+) ==')
list1 = ['a', 'b', 'c']

try:
	list2 = list1 + 'd'
except TypeError as err:
	print(err)
	print('Cannot concatenate a string into a list. Only a list can be concatenated in a list')
else:
	print(list2)

list2 = list1 + ['d']
print(list1)
print('But making the element as a list, then concatenation is possible:')
print(list2)

try:
	list3 = list2 + ('e', 'f', 'g', 'h')
except TypeError:
	print('Same happens with any other data type. Cannot concatenate tuple with a list')


print('== Using Replication Operator (*) ==')
x = ['mat', 'rix']
y = x*4
print(y)


print('== Using augmented assignment operators (+=, *=) ==')
print('= Extending list using += =')
x = ['a', 'b', 'c']
x += 'd'
print(x)

print('= Replicating list using *= =')
x = ['a', 'b', 'c']
x *= 2
print(x)


print('=== Looping elements of a list ===')
list1 = ['Science', 'Maths', 'Chemistry', 'Biology', ('Red', 'Green')]
for item in list1:
	print(item)

for index in range(len(list1)):
	print(list1[index])

for oddItem in list1[::2]:		# Printing all the odd number items of the list
	print(oddItem)

for evenItem in list1[1::2]:
	print(evenItem)


print('=== Extending a list using list.extend() method ===')
x = ['a', 'b', 'c']
y = ['z', 'y', 'x', 'w']
y.extend(x)
print(y)


print('=== Adding items in a list using list.append() method ===')
import random
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = ['a', 'b', 'c']
counter = 0
while counter < 11:
	x.append(random.choice(alphabets))		# list.append() inserts items at the end of the list
	counter += 1
print(x)


print('=== Adding items in a list using list.insert() method ===')
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
x = ['a', 'b', 'c']
counter = 0
while counter < 11:
	# list.insert() inserts items at the given index in the list
	randomIndex = random.randint(0, len(alphabets))
	randomValue = random.choice(alphabets)
	print("Inserting value: {0} at index: {1}".format(randomValue, randomIndex))
	x.insert(randomIndex, randomValue)
	counter += 1
print(x)


print('=== Adding items in a list by slicing method ===')
x = ['a', 'b', 'c']
x[1:1] = '5'
print(x)

x[1:1] = 'new 1'	# If a string of multiple characters is passed, each character will be inserted separately one by one
print(x)
