from ..base_animal import AnimalBaseClass
from importlib import import_module
import pkgutil
import os
import sys

"""
All this is doing is: 
        from .goldfish import GoldFish as goldfish

I just added it there because I'm too lazy to add this line whenever I need to add a new fish to the family.

"""

for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
    imported_module = import_module('.' + name, package='animals.fish')

    class_name = list(filter(lambda x: x != 'AnimalBaseClass' and not x.startswith('__'),
                             dir(imported_module)))

    fish_class = getattr(imported_module, class_name[0])

    if issubclass(fish_class, AnimalBaseClass):
        setattr(sys.modules[__name__], name, fish_class)
