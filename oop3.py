class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)     # call the superclass init method 
        self.color = color
    
    def speak(self):
        print("meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("bark")
    
p1 = Pet("Tim", 15)
c1 = Cat("Bill", 5, "Brown")
d1 = Dog("Jill", 12)
c1.show()
d1.show()
p1.show()
p1.speak()
c1.speak()
d1.speak()
