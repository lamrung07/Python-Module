#!/usr/bin/env python3
def ft_water_reminder() -> None:
    x = int(input("Days since last watering: "))
    if x > 2:
        print("Water the plants!")
    elif x <= 2:
        print("Plants are fine")

# ft_water_reminder()
