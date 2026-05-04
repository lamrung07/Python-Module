#!/usr/bin/env python3

class Plant:
    def __init__(self, name : str, height : float, age : int):
        self.name = name
        self.height = height
        self.age = age
    def grow(self):
        self.height += 1.2
        self.height = round(self.height, 2)
        self.age += 1
    # def age(self):
    #     self.age += 1
    def show(self):
        print(f"{self.name}: {self.height} cm, {self.age} days old")
        
        
if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    garden = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)]
    for plant in garden:
        plant.show()