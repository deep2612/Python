#Boolean Expressions
print(5 == 5) #Returns true
print(5 == 6) #Returns false
print(type(True)) #Returns type of value True i.e. Bool

#Other Types of Comparison Operators
print(5 != 6) #NotEqualTo Operator
print(5 < 6) #LessThan
print(10 > 5) #GreaterThan
print (5 is not 7)
print ( 5 is 5)

#Logical Operators(and , or , not)
print(5 == 5 and 6 == 6)
print(5 ==5 or 5 == 6)
print(not(5 == 5))

#Try and Except Blocks
inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')

