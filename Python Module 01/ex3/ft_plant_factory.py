#!/usr/bin/env python3
class Plant:
    def __init__(self, name : str, height : float, plant_age : int):
        self.name = name
        self.height = height
        self.plant_age = plant_age
    def grow(self):
        self.height += 1.2
        self.height = round(self.height, 2)
    def age(self):
        self.plant_age += 1
    def show(self):
        print(f"{self.name}: {self.height} cm, {self.plant_age} days old")

if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    garden = [
		["Rose", 45, 120],
		["Cactus", 8.5, 365],
		["Sunflower", 30.2, 14],
		["Lavender", 20.0, 60],
		["Bamboo", 150.0, 200],
	]
    for n in range(5):
        print(f"Created: ", end = '')
        plant = Plant(garden[n][0], garden[n][1], garden[n][2])
        plant.show()