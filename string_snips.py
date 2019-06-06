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
