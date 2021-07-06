
# Write a pyhton code to calcullate the permutaion (5,3)

import math

x = 5
y = 3

Permutation = math.factorial(x) / math.factorial(x-y)
print('Permutation(5, 3):', Permutation)


#Write a python code to calcullate combination (15, 3)
x = 15 
y = 3

Combination = math.factorial(x) / (math.factorial(x - y) * math.factorial(y))
print('Combination(15, 3): ', Combination)


#Write a pyhton code that takes the degee as an input form the user and convert it to the radian

x_deg = float(input('Enter an input: '))
PI = 22 / 7
x_rad = (x_deg * PI) / 180
print('Radian value: %.2f rad' %x_rad )

number = float((input('Number: ')))
square_root = math.sqrt(number)
print('Square root of %.3f is %.3f' %(number, square_root))


#Write a python code to calcullate lcm of the numbers (25, 55)
x =(25, 55)
highest_common_divisor = math.gcd(25,55)
Lcm = (x[0] * x[1]) / highest_common_divisor
print(f'LCM of (25,55) is {Lcm}')



#Ask th euser ot enter two numbers and generate two random numbers between them and find their combination

import random

num1 = int(input('Number 1: '))
num2 = int(input('Number 2: '))
randnum1 = random.randint(num1,num2)
randnum2 = random.randint(num1,num2)
if(randnum1 >= randnum2):
    Combination = math.factorial(randnum1) / (math.factorial(randnum1 - randnum2) * math.factorial(randnum2))
    print('Combination of (%d, %d) is: %.2f' %(randnum1, randnum2, Combination) )
else:
    Combination = math.factorial(randnum2)/ (math.factorial(randnum2-randnum1) * math.factorial(randnum1))
    print('Combination of (%d, %d) is: %.2f' %(randnum2, randnum1, Combination))



#Divide 1000 by 3 and print the answer with only 5 numbers after the decimal

number = (1000 / 3)
print('Division : %.5f' %number)



#Write a program to convert 108 to binary

#Use of recursive function
def decTobinary(number):
    if number > 0: 
        decTobinary(number // 2)
        print( number % 2, end = '')
   
number = 108
print(f'Binary value of {number}: ', end ='')
decTobinary(108)



#write a program to convert 1008 to hexadecimal

def decTohex(number):
    if number > 0:
        decTohex(number // 16)
        rem = number % 16
        if rem == 10:
            print('a', end='')
        if rem == 11:
            print('b', end='')
        if rem == 12:
            print('c', end='')
        if rem == 13:
            print('d', end='')
        if rem == 14:
            print('e', end='')
        if rem == 15:
            print('f', end ='')
        else:
            print(rem, end = '')
        

number = 1008
print('\nHexdecimal: ', end ='')
decTohex(1008)


#Write a summary of everything that you learn in this class:

line1 = "I learnt about the basic I/O syntax - take an imput from the user and the print them in console. I also get "
line2 = "to know about some of the datatype in python like string, int and different syntax and methods to print them."
line3 = "and about the concatenation of the string datatype in print function. And, how instead of declaring a variable"
line4= "We could just assign a value to a variable. And, most of all i learnt to do some research and literate me by my own."
print('\n')
print(line1, line2, line3, line4)
