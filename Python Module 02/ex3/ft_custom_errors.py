#!/usr/bin/env python3

class  GardenError(Exception):
	def __init__(self, message) -> None:
		self.message = message
	def __str__(self) -> str:
		return 	f"Caught GardenError: {self.message}"

class	PlantError(GardenError):
	def __init__(self, message) -> None:
		super().__init__(message)
	def __str__(self) -> str:
		return 	f"Caught PlantError: {self.message}"
	

class	WaterError (GardenError):
	def __init__(self, message) -> None:
		super().__init__(message)
	def __str__(self) -> str:
		return 	f"Caught WaterError: {self.message}"

def	raise_planterror(message):
	print("Testing PlantError...")
	try:
		raise PlantError(message)
	except PlantError as e:
		print(f"{e}\n")

def	raise_watererror(message):
	print("Testing WaterError...")
	try:
		raise WaterError(message)
	except WaterError as e:
		print(f"{e}\n")

if __name__ == "__main__":
	raise_planterror("The tomato plant is wilting!")
	raise_watererror("Not enough water in the tank!")