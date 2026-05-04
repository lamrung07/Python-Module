#!/usr/bin/env python3
def ft_harvest_total()->None:
	print("Day 1 harvest: ", end = '')
	x1 = int(input())
	print("Day 2 harvest: ", end = '')
	x2 = int(input())
	print("Day 3 harvest: ", end = '')
	x3 = int(input())
	print(f"Total harvest: {x1 + x2 + x3}")

# ft_harvest_total()