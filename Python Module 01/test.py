class Plant:
	count = 0
	def __init__(self, name, height):
		self.name = name
		self.height = height
		Plant.count += 1
	def plant_info(self):
		return f"{self.name} ||| {self.height}cm"

	@classmethod
	def get_count(d):
		return f"Total # of plants : {d.count}"


plant1 = Plant("Rose", 5)
print(plant1.plant_info())
plant2 = Plant("Tomato", 10)
print(plant2.plant_info())
plant3 = Plant("Pomme", 2)
print(plant3.plant_info())

print(Plant.get_count())