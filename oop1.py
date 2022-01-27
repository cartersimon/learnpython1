class Dog:
    def __init__(self, name):
        self.name = name # create instance var called name

    def add_one(self, x):
        return x + 1

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def bark(self):
        print('Bark')

d = Dog('Tim')
print(d.bark)