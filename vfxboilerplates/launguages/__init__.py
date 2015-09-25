
class Language(object):
    def __init__(self, keywords):
        self.keywords = keywords

    def update_keywords(self, data):
        self.keywords = data

    def header(self):
        return ""

