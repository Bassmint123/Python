# Brad casting some data types
a = input('Enter a Number: ')
b = input ('Now enter another number: ')

sum = a + b
print('\nData Type Sum :', sum, type(sum))

sum = int(a) + int(b)
print('Data Type sum :', sum, type(sum))

sum = float(sum)
print('Data Type sum :', sum, type(sum))

sum = chr(int(sum))
print('Data Type sum :', sum, type(sum), ' That is all!')
