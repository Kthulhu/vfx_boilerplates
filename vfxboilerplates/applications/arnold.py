import random


class Arnold(object):
    @property
    def name(self):
        return 'arnold'

    @property
    def maya_id(self):  # TODO: should generate random if id not provided.
        return "0x%06x" % random.randint(0, 0xFFFFFF)
