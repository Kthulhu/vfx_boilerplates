__author__ = 'fredrik.brannbacka'
import os
import inspect
from vfxboilerplates.plates import Plate

class Maya(Plate):
    def __init__(self):
        super(Maya, self).__init__()
        
    @classmethod
    def list_languages(cls):
        maya = cls()
        for module in maya.get_submodules():
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    if obj.__name__ == module.__name__.rsplit('.', 1)[-1].capitalize():
                        yield obj

    @classmethod
    def get_example(cls, name=None):
        if name:
            for language in cls.list_languages():
                return language()
        pass
