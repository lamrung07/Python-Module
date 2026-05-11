#!/usr/bin/env python3
class Plant_Secured:
	def __init__(self, name : str, height : float, age : int)->None:
		self._name = name
		self._height = 0.0
		self._age = 0
		if height < 0:
			print(f"{self._name}: Error, height can't be negative\n")
		else:
			self._height = height
		if age < 0:
			print(f"{self._name}: Error, age can't be negative\n")
		else:
			self._age = age
		print(f"Plant created: {self._name}: {self._height}cm, {self._age} days old")

	def set_height(self, height : float)->None:
		if height < 0:
			print(f"{self._name}: Error, height can't be negative\nHeight update rejected")
		else:
			self._height = height
			print(f"Height updated: {height} cm")
	def set_age(self, age : int)->None:
		if age < 0:
			print(f"{self._name}: Error, age can't be negative\nAge update rejected")
		else:
			self._age = age
			print(f"Age updated: {age} days")
	def get_height(self) -> float:
		return self._height
	def get_age(self) -> int:
		return self._age
	def show(self):
		print(f"Current state: {self._name}: {self._height} cm, {self._age} days old")

if __name__ == "__main__":
	print("=== Garden Security System ===")
	rose = Plant_Secured("Rose", 15.0, 10)
	rose.set_height(2)
	rose.set_age(99)
	rose.set_height(-5)
	rose.set_age(-3)
	print(f"Current state: {rose._name}: {rose._height}cm, {rose._age} days old\n")

