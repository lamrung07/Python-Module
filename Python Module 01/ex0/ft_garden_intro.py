#!/usr/bin/env python3

def ft_garden_intro(name: str, height: int, age: int) -> None:
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}\nHeight: {height}cm\nAge: {age} days\n")
    print("=== End of Program ===\n")


if __name__ == "__main__":
    ft_garden_intro("Rose", 27, 10)
    # ft_garden_intro("Sunflower", 80, 45)
    # ft_garden_intro("Rose", 15, 120)
