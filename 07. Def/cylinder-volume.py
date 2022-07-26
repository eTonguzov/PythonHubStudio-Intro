# расчет объема цилиндра
import math

PI = math.pi

def radius():
    n = float(input("Enter diametr cylinder in cm3: "))
    n /= 2
    return n
def height():
    m = float(input("Enter height cylinder in cm3: "))
    return m

def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s * h

    return v
print("Volume cylinder: ",  volume(), "cm3")

def massa(v):#на вход принимается объем цилиндра(причем здесь абсолютно не важно имя переменной на вход)
    n = float(input("Enter massa 1 g/cm3: "))
    return v*n/1000
print("Massa cylynder in kg ", massa(volume()))