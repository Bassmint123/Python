# Declare variables
x = 1
y = 3.789
z = 5j

# The type method will print the type of variable ie. float, int,...etc.
print(type(x))
print(type(y))
print(type(z))

# Conversions
age = 13
print "I am " + str(age) + " years old!"

# Convert to an integer
number1 = "100"
number2 = "10"

string_addition = number1 + number2 
# string_addition now has a value of "10010"

int_addition = int(number1) + int(number2)
# int_addition has a value of 110

string_num = "7.5"
print int(string_num)
print float(string_num)
