__author__ = 'fredrik.brannbacka'

from maya import Maya
from arnold import Arnold

applications = {
    'maya': Maya,
    'arnold': Arnold
}


def get(name=None):
    return applications.get(name, None)
