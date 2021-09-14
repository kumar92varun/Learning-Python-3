# Program to learn about String built-in data type
x = 'Varun'
y = "Kumar"
print(x, y, sep=' ')


print("\n========== blank string ==========")
blankString = str()		# Will give a blank string
print(blankString)


print("\n========== Converting other class objects to String ==========")
a = str('xxxx')
b = str(False)
c = str(44)
d = str(None)
e = str(56.85)
print(a, b, c, d, e, sep='\' - \'')


print("\n========== Single quoted multi-line string ==========")
# A Single quoted string - for multiple lines need to escape the newline character at the end of line 1
x = 'This is a single quoted string\
 where we need to escape \' but not "'
print(x)


print("\n========== Double quoted multi-line string ==========")
# A Double quoted string - for multiple lines need to escape the newline character at the end of lines
x = "This is a double quoted string \
where we need to escape \" but not '"
print(x)


print("\n========== Tripple quoted multi-line string ==========")
# A Tripple quoted string -  no need to escape newline characters
x = """This is tripple quoted string where we 
I am second line
This is third line => don't need to excape either " or ' """
print(x)


print("\n========== Another tripple quoted multi-line string ==========")
x = '''This is also tripple quoted string
where no escape character is required. 
And this is line 3'''
print(x)


print("\n========== Some escape characters ==========")
x = 'A tab is:\tThis. A newline is:\nThis.A backspace is:\bThis.A vertical tab is:\vThis.\vA carriage return is:\rThis right.'
print(x)
y = "1\v2\v3\v4\v5\v6"
print(y)
z = "1\r2\r3\r4\r5\r6"
print(z)


print("\n========== Significance of Raw Strings ==========")
x = "A backslash \\ with a tab \\t and vertical tab \\v and a newline \\n."
print(x)
rawString = r'A backslash \ with a tab \t and vertical tab \v and a newline \n using Raw Strings.'
print(rawString)


print("\n========== Writing multi-line strings ==========")
x = 'Line 1\
 Line 2\
 Line 3'
print(x)

y = ('Line 4'
' Line 5'
' Line 6'
)
print(y)

z = '''Line 1
Line 2
Line 3'''
print(z)


print("\n========== ord() Function ==========")
x = ord("`")		# Used to get unicode code point of a character
print(x)

print("\n========== chr() Function ==========")
x = chr(0x23B7)		# Used to get unicode character by passing the unicode code point integer value
y = chr(8734)		# Used to get unicode character by passing the unicode code point integer value
print(x, y)


print("\n========== String slicing and striding ==========")
str1 = "Varun Kumar is great!est"
print(str1[3:6])
str2 = str1[:-4] + str1[-3:] + str1[5]*20 + str1[-4]*4
print(str2)