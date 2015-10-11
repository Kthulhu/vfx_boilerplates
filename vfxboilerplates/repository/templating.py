import os
import jinja2
import codecs

class Loader(jinja2.BaseLoader):
    def __init__(self, source):
        self.source = source

    def get_source(self, environment, template):
        return template, self.source, lambda: False


class BaseTemplate(object):
    def __init__(self, source, destination, parent):
        self.parent = parent
        self.file_path = source
        self.source_template = env.get_template(codecs.open(source, encoding='utf-8', mode='r').read())
        self.destination_template = env.get_template(destination)

    def get_keywords(self):
        return {}

    def render(self, data):
        res = {}
        res['destination'] = os.path.join(self.parent.destination_dir, self.destination_template.render(data))
        data['filepath'] = res['destination']
        data['filename'] = os.path.basename(res['destination'])
        data['basename'] = os.path.splitext(data['filename'])[0]
        data['language'] = self.parent.language(data)
        data[self.parent.application.name] = self.parent.application
        res['source'] = self.source_template.render(data)
        return res


class SourceTemplate(BaseTemplate):
    def get_keywords(self):
        return dict(filename=os.path.basename(self.file_path))

def classify(value):
    return value[0].upper() + value[1:]

env = jinja2.Environment(loader=Loader(''))
env.filters['classify'] = classify