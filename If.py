
# a python program to find the largest of three numbers .

x, y, z = map(int, input("Enter three numbers: ").split())
if(x > y and x > z):
    print(f"{x} is the largest number.")
elif(y > z):
    print(f"{y} is the largest number.")
else:
    print(f"{z} is the largest number.")


#python program to check whether a character is uppercase or lowercase alphabet.
character = input("Enter a charcter: ")

if(character == character.upper()):
    print(f"%s is upper case." %character)
else:
    print(f"%s is lower case" %character )


# Python to find whether given input is number or character.
u_input = input("Enter a value: ")
if(u_input >= '0' and u_input <= '9'):
    print(f"{u_input} is a number." )
else:
    print(f"{u_input} is a character")


# a program to check whether the input alphabet is vowel or not using if-else.####
Alphabet = input("Enter an alphabet: ")
vowel = ['a', 'e', 'i' , 'o', 'u']

if(Alphabet.lower() in vowel):
    print(f"{Alphabet} is a vowel letter.")
else:
    print(f"{Alphabet} is not a vowel letter.")


#Write a program to check whether the entered year is leap year or not.
#leap year = year/4 and year % 100 != 0 or year % 4 == 0
year = int(input('Enter a year: '))
if((year % 4 == 0 and year % 100 != 0 )or (year % 400 == 0 ) ):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Write a program to check if the number is Armstrong or not.
str_num = input("Enter a number: '")
power = len(str_num)
number = int(str_num)

temp = number
sum = 0

while temp > 0:
    rem = temp % 10
    sum += sum + (rem ** power)
    temp //= 10

if(sum == number):
    print(f"{number} is an Armstronng number.")
else:
    print(f"{number} is not an Armstrong number.")


#Write a program to compute the grade from marks. 
marks = int(input('Enter marks: '))

if(marks > 90 and marks <= 100):
    print("Grade: A")
elif(marks > 80 ):
    print("Grade: B")
elif(marks > 70):
    print("Grade: c")
elif(marks > 60):
    print("Grade: D")
elif(marks > 50):
    print("Grade: E")
else:
    print("Grade: F")

