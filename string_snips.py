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

# Using the % to print variables in place of the %s
string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

