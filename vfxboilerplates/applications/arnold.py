import random


class Arnold(object):
    def __init__(self, id=None):
        self._id = id

    @property
    def name(self):
        return 'arnold'

    @property
    def maya_id(self):  # TODO: should generate random if id not provided.
        if self._id:
            return self._id
        else:
            return "0x%06x" % random.randint(0, 0xFFFFFF)
