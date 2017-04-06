## animal isa object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## dog isa animal
## dog hasa init function
class Dog(Animal):
    def __init__(self, name):
        ## dog hasa name
        self.name = name

## cat isa animal
## cat hasa init
class Cat(Animal):
    def __init__(self, name):
        ## cat hasa name
        self.name = name

## person isa object
## person hasa init function
class Person(object):
    def __init__(self, name):
        ## Person hasa name
        self.name = name

        ## Person hasa pet
        self.pet = None

## employee isa person
## employee hasa init function
class Employee(Person):
    def __init__(self, name, salary):
        ## ummmmmmmmmm wtf is this shit?
        super(Employee, self).__init__(name)
        ## employee hasa salary
        self.salary = salary

## fish isa object
class Fish(object):
    pass

## salmon isa Fish
class Salmon(Fish):
    pass

## halibut isa Fish
class Halibut(Fish):
    pass

## rover isa dog
## rover hasa name "Rover"
rover = Dog("Rover")

## satan isa cat
## satan hasa name "Satan"
satan = Cat("Satan")

## mary isa person
## mary hasa name "Mary"
mary = Person("Mary")

## mary hasa pet, satan
mary.pet = satan

## frank isa employee
## frank hasa name "Frank"
## frank hasa salary 120000
frank = Employee("Frank", 120000)

## frank hasa pet, rover
frank.pet = rover

## flipper isa Fish
flipper = Fish()

## crouse isa Salmon
crouse = Salmon()

## harry isa Halibut
harry = Halibut()
