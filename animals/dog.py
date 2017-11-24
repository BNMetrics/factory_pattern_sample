from . import AnimalBaseClass


class Dog(AnimalBaseClass):
    def __init__(self, name=None):
        AnimalBaseClass.__init__(self, name)

    def make_sound(self):
        print('woof, woof! :3')

    def move(self):
        print('the dog walks')