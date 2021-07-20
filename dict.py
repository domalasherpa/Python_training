
#Make a dictionary using lists above and delete the key-value (students:marks) pairs with lowest marks. 
Students = ['jack','jill','david','silva','ronaldo']
Marks = ['55','56' ,'57', '66' ,' 76']
dict = {}

for i in range(len(Students)):
    dict[Students[i]] = Marks[i]

del dict[min(dict.keys())]
print(dict)


#Euro = {‘France’:5,’Germany’:2,’Portugal’:3,’Hungary’:6}
#Make two lists from above dictionary

Euro = {'France': 5, 'Germany': 2, 'Portugal' : 3, 'Hungary': 6}
country =[]
point = []

for key,value in Euro.items():
    country.append(key)
    point.append(value)

print(country)
print(point)


#users = {'g91':{'name':'Aron','age':55,'poison':'Old monk'},
#        'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
#        'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
#Generate a list of usernames, name, age and poison from the above dictionary.
#Take the above list and put it in order.

users = {'g91': {'name': 'Aron', 'age': 55, 'poison': 'Old monk'},
         'twir56':{'name':'Visakha','age':26,'poison':'coca cola'},
         'jsdl8':{'name':'Saudi','age':12,'poison':'hinwa'}}
username = []
values = []
name = []
age = []
poison = []
for key, value in users.items():
    username.append(key)
    values.append(value)

for i in range(len(values)):
    name.append(values[i]['name'])
    age.append(values[i]['age'])
    poison.append(values[i]['poison'])

print(name)
print(age)
print(poison)


#Create an empty dictionary called milk_carton. Add the following key/value pairs.You can make up the values or use a real milk carton.
#Expiration_date: a tuple with day, month, year
#Vol: volume of milk 
#Cost: cost of milk
#Brand_name
#Print out the values of all of the elements of the milk_carton using the values in the dictionary.
#Show how to calculate the cost of six cartons of milk based on the cost of the milk_carton.
milk_carton = {}
milk_carton['Expiration_date'] = (18, 'January', 2021)
milk_carton['Volume'] = '40 ml'
milk_carton['Cost'] = 40
milk_carton['Brand_name'] = 'DDC'

print(milk_carton.values())

no_of_carton = int(input("Enter the number of the milk carton: "))
cost = no_of_carton * milk_carton['Cost']

print(f"Cost of {no_of_carton} is Rs.{cost}.")
