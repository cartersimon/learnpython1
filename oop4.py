class Person():
    number_of_people = 0    # class attribute, handy for constants, or variabes that will be used by all instances of the class

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod                        # marks this method as a class method, rather than an instance class
    def get_number_of_people(cls):          # "self" not used here as it's not acting on an instance, uses "cls" to specify to act on the class
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")

print(Person.number_of_people)
print(p2.number_of_people)  # calling the class attribute, rather than instance attribute