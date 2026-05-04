#!/usr/bin/env python3
from ft_garden_data import Plant

def simulate_week(plant : Plant) -> None:
    print("=== Garden Plant Growth ===")
    plant.show()
    start_height = plant.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        plant.grow()
        plant.show()
    growth = round(plant.height - start_height, 2)
    print(f"Growth this week: {growth}cm")

if __name__ == "__main__":
    rose = Plant("Rose", height=25.0, age=30)
    simulate_week(rose)
        
