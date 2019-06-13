
# Gonna be using <, !=, >, <=, ==, >= in the next few lines

bool_one = 3 < 5  # Evaluates to True  

bool_two = 100 != 100 # Evaluates to False

bool_three = 15 > 10 # Evaluates to True

bool_four = 34 < 5 # Evaluates to False

bool_five = 14 <= 15 # Evaluates to True

bool_six = 5 == 5 # Evaluates to True

bool_seven = 6 >= 5 # Evaluates to True

# Gonna do some booleans here using AND

bool_one = False and False 
print (bool_one) # Evaluates to False

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True 
print (bool_five) # Evaluates to True

# Gonna do some booleans here using OR

bool_one = 100 ** 0.5 >= 50 or False
print (bool_one)

bool_two = False or False
print (bool_two)

# The order of boolean evaluation is: not, and, or
bool_one = False or not True and True
print(bool_one)
bool_two = False and not True or True
print(bool_two)
bool_three = True and not (False or False)
print(bool_three)
bool_four = not not True or False and not True
print(bool_four)
bool_five = False or not (True and True)
print(bool_five)



