def GCD(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def LCM(num1, num2):
    if num1 <  num2:
        limit = num1
    else:
        limit = num2
    for i in range(1, limit + 1):
        if(num1 % i == 0) and (num2 % i == 0):
            hcf = i 
    lcm =(num1 // hcf) * (num2 // hcf) * hcf
    return lcm

    
    