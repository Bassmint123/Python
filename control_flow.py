
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

# Using if statements with methods
def using_control_once():
    if (4 < 5):
        return "Success #1"

def using_control_again():
    if (5 == 5):
        return "Success #2"

print using_control_once()
print using_control_again()

# Using if with elif else
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)




