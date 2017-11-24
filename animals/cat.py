from . import AnimalBaseClass


class Cat(AnimalBaseClass):
    def __init__(self, name=None):
        AnimalBaseClass.__init__(self, name)

    def make_sound(self):
        print('meowwww! :3')

    def move(self):
        print('the cat walks')

    def purr(self):
        print('purrrrr!<3')

