from beginner.oop.extends.animal import Animal
from beginner.oop.extends.flyable import Flyable
from beginner.oop.extends.runnable import Runnable


class Bird(Animal, Runnable, Flyable):
    pass


b = Bird()
print()
b.fly()
b.run()
