#Homework 1: Print Range (Done)
"""
start_var , end_var = map(int, input('Pls Enter Staring and ending value: ').split())

for iterator in range(start_var,(end_var+1)):
    print(iterator)

"""
#Homework 2: Repeat Me(Done)
"""
N , S = input('Enter Integer N , String S: ').split()
N =  int(N)
iterator = 0
while iterator!=N:
    print(S)
    iterator +=1
"""

#Homework 3: Print face down left angled triangle
"""
N = int(input('Pls Enter Integer N: '))
print(N)
iterator = N 
star = '*'
while iterator != 0:
    print(iterator * star)
    iterator -=1
"""

#Homework 4: Special Average (Done)
"""
N = int(input('Pls Enter Integer N: '))
even_positions = odd_positions = 0
for Iterator in range(N):
    number = int(input())
    if Iterator % 2 == 0:
        #Position is even
        even_positions +=number
    else:
        odd_positions +=number
print('avg of even positions is',even_positions/ 3)
print('avg of odd positions is',odd_positions/ 3)

print('Finish')
"""

#Special Calculator
"""
print('Menu:\nEnter 1 to sum numbers from 1 to N\nEnter 2 to evalute simple 2 numbers expression (e.g. 2 + 3)\nEnter 3 to end the program')

Num_choice = int(input('Enter choice from 1 to 3: '))
if Num_choice == 1:
    Num = int(input('Enter a number: '))
    sum = 0
    for item in range(Num):
        sum += item
    print('Sum from 1 to',Num,'to',sum)

elif Num_choice == 2:
    Num1, operation, Num2 = input('Enter a simple expression: ').split()
    Num1 , Num2 = float(Num1), float(Num2)

    if operation == '+':
        res = Num1 + Num2
    elif operation == '-':
        res = Num1 - Num2
    elif operation == '*':
        res = Num1 * Num2
    elif operation == '/':
        if Num2 == 0:
            print('Sorry: No way to compute this expression')
        res = Num1 / Num2
    elif operation == '//':
        if Num2 == 0:
            print('Sorry: No way to compute this expression')
        res = Num1 // Num2
    elif operation == '**':
        res = Num1 ** Num2
    elif operation == '%':
        res = Num1 % Num2

    print('Expression Value is',res)

elif Num_choice == 3:
    pass

else:
    print('Invalid Input...Try again')

"""
#Homework 1: Print Diamond
"""
var = int(input('Enter Integer N: '))
print(var)

i = 1
for item in (range((var), 0 , -1)):
    print( item * ' ', i * '*')
    i +=2

i -=2
for item in (range(1 , (var +1))):
    print( item * ' ', i * '*')
    i -=2
"""

#Homework 2: Special multiples 1

"""
num  = int(input('Enter a Integer num: '))

for item in range(num):
    if  item % 8 == 0 or item % 12 == 0:
        even = item % 2
        print(item, end=' ')
"""

#Homework 3: Special multiples 2


#Homework 4: Minimum of values
#Homework 1: Find NOs
#Homework 2: Reverse number
#Homework 3: Multiplication table
#Homework 4: Special Sum
#Recall: Special Sum Homework
#Practice: Special Sum
#Practice: Special Sum - using power operator
#Practice: Pair of numbers
#Practice: Pair of numbers - FASTER
#Practice: Triples of numbers
#Practice: Triples of numbers - FASTER
#Homework 1: Printing X
#Homework 2: Find Special Pairs
#Homework 3: Find all quadruples
#Homework 4: Is Prime?
#Homework 5: Print Primes
#Homework 6: Digits sum in range
