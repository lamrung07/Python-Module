#!/usr/bin/env python3
def ft_count_harvest_iterative() -> None:
    x = int(input("Days until harvest: "))
    for day in range(1, x + 1):
        print(f"Day {day}")
    print("Harvest time!")

# ft_count_harvest_iterative()
