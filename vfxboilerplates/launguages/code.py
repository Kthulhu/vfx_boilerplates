class Code(object):
    def __init__(self, keywords):
        self.keywords = keywords

    def update_keywords(self, data):
        self.keywords = data

    @property
    def header(self):
        return ""

    @property
    def footer(self):
        return ""
