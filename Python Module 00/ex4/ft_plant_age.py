#!/usr/bin/env python3
def ft_plant_age()->None:
	print("Enter plant age in days: ", end = '')
	x = int(input())
	if x > 60:
		print ("Plant is ready to harvest!")
	elif x <= 60:
		print("Plant needs more time to grow.")

# ft_plant_age()