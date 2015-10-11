import random


class Maya(object):
    @property
    def name(self):
        return 'maya'

    @property
    def id(self):  # TODO: should generate random if id not provided.
        return "0x%06x" % random.randint(0, 0xFFFFFF)
