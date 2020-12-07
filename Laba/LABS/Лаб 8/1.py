class Dog:
    gav = lambda self: print("Gav!!")
class Cat:
    meow = lambda self: print("Meow!!")
dog = Dog()
cat = Cat()
dog.gav()
cat.meow()