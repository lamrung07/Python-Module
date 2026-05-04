#!/usr/bin/env python3
def ft_water_reminder()->None:
	print("Days since last watering: ", end ='')
	x = int(input())
	if x > 2:
		print("Water the plants!")
	elif x <= 2:
		print("Plants are fine")

# ft_water_reminder()