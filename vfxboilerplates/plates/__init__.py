import os
import vfxboilerplates as vfxb
import pkgutil
import inspect

class Plate(object):
    def __init__(self):
        self.root_path = os.path.dirname(os.path.abspath(inspect.getfile(self.__class__)))
        self.module_path = "%s.plates" % (vfxb.__name__)

    def get_submodules(self):
        for importer, package_name, _ in pkgutil.iter_modules([self.root_path]):
            full_package_name = "%s.%s" % (self.module_path, package_name)
            module = importer.find_module(package_name).load_module(full_package_name)
            yield module

    @classmethod
    def list_subclasses(cls):
        plate = cls()
        for module in plate.get_submodules():
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj):
                    if obj.__name__ == module.__name__.rsplit('.', 1)[-1].capitalize():
                        yield obj

    @classmethod
    def get_plate(cls, name=None):
        for plate in cls.list_subclasses():
            if plate.__name__.lower() == name.lower():
                return plate()
        return None


def get_plate(name=None):
    if name:
        for plate in Plate.list_subclasses():
            if plate.__name__.lower() == name.lower():
                return plate()
    return None

if __name__ == '__main__':
    plate = Plate.get_plate('maya')
    print plate, plate.list_plates()