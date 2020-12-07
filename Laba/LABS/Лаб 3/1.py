class Animal():
	def __init__(self, name):
		self.name = name
	def makeNoise(self):
		pass

class Dog(Animal):
	def makeNoise(self):
		print(self.name + "says: Gav")
class Cat(Animal):
	def makeNoise(self):
		print(self.name + "says: Meow")
		
dog = Dog("Dog")
cat = Cat("Cat")
dog.makeNoise()
cat.makeNoise()
