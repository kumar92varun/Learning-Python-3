# Program to learn about Tuple built-in data type

print('\n\n=== Creating tuples ===')
x = tuple()
print(x)

x = (1, 2, 3, 4)
print(x)

x = 1, 2,
print(x)

x = (1,)
print(x)

x = 1
y = 1,
print(type(x), type(y))


print('\n\n=== Some basic tuple operations ===')
x = 'Venus', -28, "Green", 21.56, True, False, 'Jin Kazama'
print(x)
print(len(x))
for member in x:
	print(type(member), 'and value is:', member)

y = x*9
print(y)
print('Length of this tuple is:', len(y))
print(y.count(-28))
print(y.index(21.56))

try:
	print(y.index('rrr'))
except ValueError as err:
	print('rrr is not in tuple')


print('\n\n=== Using + operator with Tuple ===')
a = 1,2
b = (3,)
c = tuple()
d = 4,
e = a + b + c + d
print(e)


print('\n\n=== Using * operator with Tuple ===')
a = 1, 2
b = (3,)
c = tuple()
d = 4,
e = a + b + c + d
f = 6 * e
g = e * 2
print(f)
print(g)


print('\n\n=== Using += operator with Tuple ===')
p = 7,6,8,10,59
q = 'A', "b", 44, 'D', 
q += (4,)
print(q)


print('\n\n=== Using *= operator with Tuple ===')
p = ('a', 'b', 'c')
p *= 2
print(p)


print('\n\n=== Nesting tuples inside tuple ===')
x = ('a', 'b', (3, 4, 5, 6), 'c', (55.66,), 'd')
print(type(x[4]))


print('\n\n=== Sequence unpacking ===')
name, age, hobbies = ('Varun Kumar', 16, ('Coding', 'Programming', 'Trance'))
print('Name is:', name)
print('Age is:', age)
print('Hobbies are:', hobbies)


print('\n\n=== Another example of sequence unpacking ===')
manufacturer, model, seating = (0, 1, 2)
minimum, maximum = 0, 1
aircraft = ('Airbus', 'A320', (100, 500))
print("Minimum number of seats in this aircraft is:", aircraft[seating][minimum])


print('\n\n=== Yet another example of sequence unpacking ===')
for CURRENCY, RATE in (('$', 1), ('Rs.', 75.699), ('Euro', 8)):
	print("Currency", CURRENCY, "has an exchange rate of", RATE)


print('\n\n=== Named Tuples ===')
import collections

Student = collections.namedtuple('my_student_custom_data_type', 'name age hobbies skills')
Varun = Student('Varun Kumar', 16, ['Trance', 'Swimming', 'Coding', 'Programming'], ['PHP', 'Python', 'JavaScript'])
print(Varun)
print(type(Varun))
Anshul = Student("Anshul Nagpal", 29, ['Rona', "Dhona"], ('Sleeping', 'Walking'))
print(Anshul)
print(type(Anshul))

Mobile = collections.namedtuple('A_cell_phone', ['company', 'model', 'price'])
SamsungS30 = Mobile('Samsung', 'S30', 'Rs. 15,500')
print(SamsungS30.price)