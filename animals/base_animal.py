from abc import ABCMeta, abstractmethod


class AnimalBaseClass(metaclass=ABCMeta):
    def __init__(self, name=None):
        if name:
            self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass
