from importlib import import_module

from .base_animal import AnimalBaseClass


def grab(animal_name, *args, **kwargs):

    try:
        if '.' in animal_name:
            module_name, class_name = animal_name.rsplit('.', 1)
        else:
            module_name = animal_name
            class_name = animal_name.capitalize()

        animal_module = import_module('.' + module_name, package='animals')

        animal_class = getattr(animal_module, class_name)
        assert issubclass(animal_class, AnimalBaseClass)

        instance = animal_class(*args, **kwargs)

    except (AttributeError, AssertionError, ModuleNotFoundError):
        raise ImportError('{} is not part of our animal collection!'.format(animal_name))

    return instance
