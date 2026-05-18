#!bin/usr/env python3
import math

def check_input(n):
    try:
        n = float(n)
    except:
        raise ValueError (f"Error on parameter '{n}':")
    pass
def get_player_pos():
    pos = [None] * 3
    while True:
        try:
            x,y,z = input("Enter new coordinates as floats in format 'x,y,z': ").split(',')
            check_input(x)
            check_input(y)
            check_input(z)
        except:
            print("Invalid systax")
        else:
            break

get_player_pos()