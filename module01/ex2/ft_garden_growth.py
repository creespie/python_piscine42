class	Plant:
	instances = []

	def	__init__(self, name: str, height: float, ages: int, growth_rate: float = 0.8):
		self.name = name
		self.height = height
		self.ages = ages
		self.growth_rate = growth_rate
		Plant.instances.append(self)
	
	def	__str__(self):
		if self.ages != 1:
			return (f"{self.name.capitalize()}: {self.height}cm, {self.ages} days old")
		else:
			return (f"{self.name.capitalize()}: {self.height}cm, {self.ages} day old")

	def	show(self):
		print("=== Garden Plant Registry ===")
		for instance in Plant.instances:
			print(instance)
	
	def	age(self):
		self.ages += 1

	def	grow(self):
		self.height = round((self.height + self.growth_rate), 1)

if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 1)
    print("=== Garden Plant Growth ===")
    print(rose)
    start_height = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        print(rose)
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")