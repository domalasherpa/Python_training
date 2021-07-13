
# Convert tuples to list.

import math 

tuple = (1, 2, 3, 4, 'a', 'b', "apple", "ball")
reset = list(tuple)
#To check if we can  manipulate single element.
reset[1] = 8
print(reset)


# Write a program to calculate direction and magnitude of the vector described by the following points.
# A = (20,30)   #x1, y1
#B = (30,40)    #x2, y2

#magnitude = sqrt((x2-x1)^2 + (y2-y1)^2)
#direction = tan-1(y2-y1 / x2-x1)

A = (20, 30)
B = (30, 40)
x_component = B[0] - A[0]
y_component = B[1] - A[1]

Magnitude = math.sqrt(pow(x_component, 2) + pow(y_component, 2))
Direction = math.atan(y_component / x_component)
PI = 3.14
Angle = (Direction * 180) / PI    

print("Magnitude: %.3f" %Magnitude)
print("Direction: %.2f degrees" %Angle)


#Write a program to demonstrate data types that can be elements of a tuple.

Tuple = ((1, 2, 3), [1, 'a', "hello"], 'a', 1)
print(Tuple)
print("Datatype: " +str(type(Tuple[0])))
print("Datatype: " +str(type(Tuple[1])))
print("Datatype: " +str(type(Tuple[2])))
