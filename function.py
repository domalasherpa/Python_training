#import
import math
import factor


#Write a function that calculates the X^Y 
def power(base, exp):
    value = 1
    while exp != 0:
        value = value * base
        exp -= 1
    return value


#Write a Python function to multiply all the numbers in a list.
def list_mul(list):
        mul = 1
        for list in list:
            mul = list * mul
        return mul 


#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(number):
    factorial = 1
    if number == 0:
        print(1)
    elif (number > 0):
        while number != 0:
            factorial = factorial * number
            number = number - 1
        print(factorial) 
    else:
        print("factorial does not take negative number")


#Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters.
def caseCounter(str):
    count_upper = 0
    count_lower = 0
    for string in str:
        if string == string.upper():
            count_upper += 1  
        else:
            count_lower += 1    
    print("Lowercase letter : ", count_lower) 
    print("UpperCase letter : ", count_upper)        


#Write a Python function that takes a list and returns a new list with unique elements of the first list
def setList(list):
    new_list = []
    while list:
        pop = list.pop()
        while pop in list :
            list.remove(pop)
        if pop != []:
            new_list.append(pop)
    return new_list
    

#Write a Python program to print the even numbers from a given list.
def evennumbers(list):
    evennumbers = []
    for number in list:
        if type(number) == int:
            if (number <= 9) and (number >= 0):
                if number % 2 == 0:
                    evennumbers.append(number)
    return evennumbers


# Write a Python function to check whether a string is a pangram or not. 
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
def pangram(str):
    A = ['a', 'b', 'c', 'd', 'e',
         'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 
         'p', 'q', 'r', 's', 't', 
         'u', 'v', 'w', 'x', 'y', 
         'z']
    for string in str:
        string = string.lower()
        while string in A:
            A.remove(string)
    if(A == []):
        print("pangram")
    else:
        print("Not pangram")


#Write a Python program that accepts a hyphen-separated sequence of words as input and 
# prints the words in a hyphen-separated sequence after sorting them alphabetically
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow
def sort(str):
    str = str.split('-')
    str.sort()
    sort = ''
    limit = len(str)
    for i in range(len(str)):
        if i < limit - 1:
            sort = sort + str[i] + '-'
        else:
            sort = sort + str[i]
    print(sort)

x= 'green-red-yellow-black-white'
sort(x)


#Write a Python program to reverse a string.
def reverse(str):
    string = ''
    for x in str:
        string = x + string             
    return string


#Write a Python program to access a function inside a function
def factorial(number):
    if number > 0 :
       return number * factorial(number - 1)
    elif number == 0:
        return 1
    else:
        return "factorial doesnot take negative number"


#Write a program to double a given number and add two numbers using lambda()?
add = lambda x, y : x + y
double = lambda x : 2*x
print(add(1,2))
print(double(8))


#Write a python module with two functions:
#GCD
#LCM
#refer to eulids extended algorithm
x = factor.GCD(33,12)
print(x)

x = factor.LCM(33, 22)
print(x)


#Write three different functions to calculate the mean, variance and standard deviation of the following data.
#You need to call your mean function to within your variance and standard deviation functions.
def mean(list):
    list.sort()
    Mean = sum(list)/ len(list)
    return Mean

def variance(list):
    Mean = mean(list)
    variance = sum((number - Mean) ** 2 for number in list) / len(list)
    return variance
    
def standard_deviation(list):
    Mean = mean(list)
    Standard_Deviation = math.sqrt(sum((number - Mean) ** 2 for number in list) / len(list))
    return Standard_Deviation
