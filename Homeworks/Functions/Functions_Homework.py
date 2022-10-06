#Homework 1: Special Multiplication (Done)

"""
#function definition
def special_multiplication(string ):
    i = 1
    for item in 'abcxf':
        print(item * i,end='')
        i +=1

special_multiplication('ahmed' )
"""

#Homework 2: Max of 6 numbers(Done)

"""
def my_max2(a, b):
    if a > b:
        return a
    return b

def my_max3(a, b, c):
    ans = my_max2(a, b)
    if ans > c:
        return ans
    return c

def my_max4(a, b, c, d):
    ans = my_max3(a, b, c)
    if ans > d:
        return ans
    return d

def my_max5(a, b, c, d, e):
    ans = my_max4(a, b, c, d)
    if ans > e:
        return ans
    return e

def my_max6(a, b, c, d, e, f):
    ans = my_max5(a, b, c, d, e)
    if ans > f:
        return ans
    return f

print(my_max6(5, 50, 8, 2, 10, 3))

"""

#Homework 3: Get nth-prime (try)
"""
def is_prime(num):
    if num :
        return True

def nth_prime(n):


for i in range (1 , 10):
    print(i, nth_prime(i))

"""
#Homework 4: Get nth-fibonacci (TRY)

"""
def nth_fib(n):
    for item in range(n):
        nth_num += item  
        return 0 


for i in range(1, 10):
    print(i , nth_fib(i))

"""
#Recall: Special Calculator
def print_menu():
    print('Menu:\nEnter 1 to sum numbers from 1 to N\nEnter 2 to evalute simple 2 numbers expression (e.g. 2 + 3)\nEnter 3 to end the program')

def sum_1_to_n():
    Num = int(input('Enter a number: '))
    sum = 0
    for item in range(Num):
        sum += item
    print('Sum from 1 to',Num,'to',sum)

def divide(Num1, operation, Num2):
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



divide(1, '-' , 1)