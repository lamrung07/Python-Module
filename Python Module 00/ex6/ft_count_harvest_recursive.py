#!usr/bin/env python3
def ft_recursive(current_day: int, harvest_day: int) -> None:
    print(f"Day {current_day}")
    if current_day == harvest_day:
        print("Harvest time!")
        return
    else:
        ft_recursive(current_day + 1, harvest_day)


def ft_count_harvest_recursive() -> None:
    harvest_day = int(input("Days until harvest: "))
    ft_recursive(1, harvest_day)

# if __name__ == "__main__":
# 	ft_count_harvest_recursive()
