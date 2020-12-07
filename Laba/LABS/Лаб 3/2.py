class Cat:
	def __init__(self, name):
		self.name = name
	def meow(self):
		print("My" + " name is " + str(self.name))
		
cat = Cat("Katty")
cat.meow()
