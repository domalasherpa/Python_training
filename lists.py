
#Make a list of ten students in your class. Print the name of each student whose name starts with ‘B’.
Name = ['Brain', 'Bobby', 'Brace', 'Bob', 'BamBam', 'Brown', 'Bandy', 'Bdion', 'Balika', 'Bartika']

#Make a list of ten students in your class. Print the name of each student whose name ends with ‘a’.
Name = ['Andy', 'Ash', 'Ace', 'Arial', 'Aries', 'Asepa', 'Arika', 'Aadi', 'Alisha', 'Andrew']
print(Name)

#Print all the unique elements in the following list 
fifa = ['Italy','Argentina','Germany','Brazil','France','Brazil','Italy','Spain','Germany','France']
fifa = set(fifa)
print(fifa)

#Change the first alphabet of all elements of the following list to capital.
Bob = ['hurricane','tambourine','blowing','numb']
Bob = [x.title() for x in Bob]
print(Bob)

A = ['a', 'b', 'c','d']
A = [a.title() for a in A]
print(A)

B = ['1', 'a', '2', 'b']
B = [b.title()for b in B]
print(B)



#Find  and 
#Calculate the mean and standard deviation of the following list:
import math 

Numbers = [1,2,3,5,88,99,55,33,41,52]

Numbers.sort()
print(Numbers)

Mean = sum(Numbers)/ len(Numbers)
print(Mean)

Standard_Deviation = math.sqrt(sum((number - Mean) ** 2 for number in Numbers) / len(Numbers))
print(Standard_Deviation)

            

