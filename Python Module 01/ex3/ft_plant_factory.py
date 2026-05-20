#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def grow(self) -> None:
        self.height += 1.2
        self.height = round(self.height, 2)

    def age(self) -> None:
        self.plant_age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height} cm, {self.plant_age} days old")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    garden: list[tuple[str, float, int]] = [
        ("Rose", 45.0, 120),
        ("Cactus", 8.5, 365),
        ("Sunflower", 30.2, 14),
        ("Lavender", 20.0, 60),
        ("Bamboo", 150.0, 200),
    ]
    for n in range(0, 5):
        print("Created: ", end='')
        plant = Plant(garden[n][0], garden[n][1], garden[n][2])
        plant.show()
