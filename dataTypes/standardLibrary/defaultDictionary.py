# Program to learn about Default Dictionaries - provided by Python's Standard Library
'''
The only difference between in-built dictionary data type and the standard library's default dictionary is that 
if a non-existent key is called in dictionary, it will raise a KeyError exception.

Whereas if a non-existent key is called in default dictionary, it won't raise KeyError exception, instead it will create 
a new key and assign it a default value (set by us).
==> Default dictionaries can never raise a KeyError exception.
'''

import collections

d1 = dict(name='Varun', age=14)
print(d1['name'])

d2 = collections.defaultdict(int)		# The parameter <int> will be the default value for a non-existent key
print(d2['name'])
d2['age'] += 1

d3 = collections.defaultdict(tuple)
print(d3['name'])
d3['full_name'] += ('Kumar', 'Varun')

d4 = collections.defaultdict(str)
print(d4['name'])


print(d1, d2, d3, d4, sep='\n')
