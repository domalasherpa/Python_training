

##program to remove the duplicate from the list,

bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
new_bird = []
while bird:
    pop_bird = bird.pop()
    while pop_bird in bird:
        bird.remove(pop_bird)
    if pop_bird != []:
        new_bird.append(pop_bird)
print(new_bird)


##program to list the sandwiches made with an message 

sandwich_orders = [' Normal Chicken', 'Fish', 'Fried Egg', 'Grilled Cheese', 'Ham', 'Ice-Cream']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your" + ' ' + sandwich + ' ' + 'sandwich.')
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)



##program that polls users and prints the output

vacation = []
poll = True

while poll: 
    prompt = input("If you could visit one place in the world, where would you go?")
    vacation.append(prompt)
    status = input("DO you want to continue ? y/n: ")
    if status == 'n':
        poll = False

#to print the result of the poll
while vacation:
    place = vacation.pop()
    count = vacation.count(place) + 1
    
    while place in vacation:
        vacation.remove(place)

    print(f'{place.title()} : {count}')
  
