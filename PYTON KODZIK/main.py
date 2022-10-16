from math import pi
from math import e 

def v_szescian():
    a = float(input("podaj a: "))
    return a**3

def v_ostroslup_czworokatny():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    return (a**2) * (1/3) * h

def v_walec():
    r = float(input("podaj r: "))
    h = float(input("podaj h: "))
    return pi * r**2 * h
 
def v_kuli():
    r = float(input("podaj r: "))
    return (4/3) * pi * r**3
 
def v_piramidy():
    a = float(input("podaj a: "))
    h = float(input("podaj h: "))
    return a**2 * h / 3

def p_kwadratu():
    a = float(input("podaj a: "))
    return (a**2)

def p_prostokatu():
    a = float(input("podaj a: "))
    b = float(input("podaj b: "))
    return (a*b)
