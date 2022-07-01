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
def massa(g):
    n = float(input("Enter massa 1 g/cm3: "))
    return g*r/1000
 print("Massa cylynder in kg ". massa(volume))


# print("Volume cylinder: ",  volume(), "cm3")
