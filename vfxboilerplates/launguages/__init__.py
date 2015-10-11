from cpp import Cpp

languages = {
    'cpp': Cpp
}


def get(name=None):
    return languages.get(name, None)
