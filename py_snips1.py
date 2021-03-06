# Appending a string
print("This is a string " + "that has been appended")

# Using triple quotes for a multi-line string
haiku = """The old pond,
A frog jumps in: 
Plop!"""

print haiku

"""
This is an inline
comment that can be used
anywhere in the code.
"""

skill_completed = "Python Syntax"
exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed*points_per_exercise

print("I got " + str(point_total) + " points!")

# Using the escape backslash!
'This isn\'t flying, this is falling with style!'


# Printing the fifth letter in the word MONTY
fifth_letter = "MONTY"[4]
print fifth_letter

# Using some string operators
parrot = "Norwegian Blue"
print len(parrot)      # Gives the length of the word parrot
print parrot.lower()   # Prints Norwegian Blue in all lower case
print parrot.upper()   # Prints Norwegian Blue in all upper case

# Convert a number to a string
pi = 3.1415
print str(pi)

"""
Using the % to print variables in place of the %s. 
You need the same number of %s terms in a string as the number of variables in parentheses
"""
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

# Getting the input function into action
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# In this case we can setup the string in a variable with %s, %d, $f, %x used within in it.
# Notice the variable data is not using set notation like data=[x,y,z] 
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

