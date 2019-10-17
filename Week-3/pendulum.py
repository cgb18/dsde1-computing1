import math

def period(L,g):
    if isinstance (L,float):
        pass
    elif isinstance (L,int):
        pass
    elif isinstance (g,float):
        pass
    elif isinstance (g,int):
        pass
    if isinstance (L,str):
        L = float(input('TypeError. Please enter a number: '))
        T = 2 * math.pi * math.sqrt(L/g)
    elif isinstance (g,str):
        g = float(input('TypeError. Please enter a number: '))
        T = 2 * math.pi * math.sqrt(L/g)
    else: 
        L = float(input('ValueError. Please enter a number: '))
        
    T = 2 * math.pi * math.sqrt(L/g)
    return T

print(period('h',9.8))