# In python 3 there is no need to put object in the paramaters of a parent class, but it's better to
# be explicit over implicit
class Animal(object):
    # Does nothing, but can be used when something is expecting an action but you don't have anything yet
    pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        # Calls the __init__ of the parent (Person) with the data name and Employee as the object
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
# sets mary's pet to satan the Cat
mary.pet = satan
frank = Employee("Frank", 120000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()