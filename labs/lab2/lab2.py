'''
Lex King
lab2.py
This code calculates the rms, harmonic mean, and geometric mean. The user inputs how many values and what the values are.
This is my code
'''
import math

def means():
    values = eval(input("How many values will you enter? "))
    rms = 0
    harmonic_mean = 0
    geometric_mean = 1
    for i in range(values):
        enter_values = eval(input("enter value: "))
        print(enter_values)
        rms = rms + enter_values**2
        harmonic_mean = harmonic_mean + 1 / enter_values
        geometric_mean = geometric_mean * enter_values
    rms_div = rms / values
    root = math.sqrt(rms_div)
    print("Root mean square:", root)
    harmonic_div = values / harmonic_mean
    print("Harmonic mean: ", harmonic_div)
    geometric_root = geometric_mean**(1 / values)
    print("Geometric mean: ", geometric_root)
