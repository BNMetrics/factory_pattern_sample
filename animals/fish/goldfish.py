from ..base_animal import AnimalBaseClass


class GoldFish(AnimalBaseClass):
    def __init__(self, name=None):
        AnimalBaseClass.__init__(self, name)

    def make_sound(self):
        print('oooOOOooooOOO..(this is supposed to be bubbles :P)')

    def move(self):
        print('the gold swims across the tank')