#Maatric multiplication
# A = 1 2 3
#     4  5  6
#     7  8  9
# 
# 111  22  33 
# 44  55  56
# 47  86   19 

x  = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

y  = [[111, 22, 33 ],
      [44, 55, 56],
      [47, 86, 19 ]]

mul = [[0, 0, 0 ],
       [0, 0, 0 ],
       [0, 0, 0 ]]


for i in range(len(x)):              #rows of x
    for j in range(len(y[0])):      #coloumn of y
        for k in range(len(y)):      #rows of y
            mul[i][j] += x[i][k] * y[k][j]
    
for mul in mul:
    print('x * y = ', mul)


        
c = [[111, 22, 33, 44],
     [44,  55, 56,  1],
     [47,  86, 19,  2], 
     [1,   2,  22,  3]]

d = [[11, 22,  3,  4], 
     [4 ,  5,  6,  1], 
     [7 ,  6, 19,  2],
     [1 ,  2, 22,  3]]

    
mul = [[0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0]]

for i in range(len(c)):                     #rows of x
    for j in range(len(d[0])):               #coloumn of y
        for k in range(len(d)):             #rows of y
            mul[i][j] += c[i][k] * d[k][j]  
    
for mul in mul:
    print('c * d = ',mul)



#F
#FFF
#FFFFF
#FFFFFFF
#FFFFFFFFF
#FFFFFFFFFFF

for i in range(6):
    for j in range(i + (i -1)):
        print('F', end = '')  
    print('')

print('')        

                                   #fibonccci pattern:
#F                                      1
#F                                      1
#FF                                     2
#FFF                                    3
#FFFFF                                  5
#FFFFFFFF                               7
#FFFFFFFFFFFFF                          12
#FFFFFFFFFFFFFFFFFFFFF                  19
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF     31

x = 0
y = 1 
for i in range(8):
    z = x + y                   
    x = y
    y = z
    for j in range(x):
        print('F', end = '')
    print('')