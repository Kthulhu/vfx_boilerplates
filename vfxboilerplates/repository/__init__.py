# -*- coding: utf-8 -*-
__author__ = 'fredrik.brannbacka'
import vfxboilerplates as vfxb
import os
import yaml
import jinja2
import codecs
from vfxboilerplates.launguages.cpp import Cpp

REPOSITORY = {}
repo_dir = os.path.abspath(os.path.join(vfxb.ROOT_DIR, "..", "repository"))

class MyLoader(jinja2.BaseLoader):
    def __init__(self, source):
        print "HERE"
        self.source = source

    def get_source(self, environment, template):
        return template, self.source, lambda: False

def classify(value):
    return value[0].upper() + value[1:]

env = jinja2.Environment(loader=MyLoader(''))
env.filters['classify'] = classify

class BaseTemplate(object):
    def __init__(self, source, destination, parent):
        self.parent = parent
        self.file_path = source
        self.source_template = env.get_template(codecs.open(source, encoding='utf-8', mode='r').read())
        self.destination_template = env.get_template(destination)
        self.language = Cpp

    def get_keywords(self):
        return {}

    def render(self, data):
        res = {}
        res['destination'] = os.path.join(self.parent.destination_dir, self.destination_template.render(data))
        data['filepath'] = res['destination']
        data['filename'] = os.path.basename(res['destination'])
        data['basename'] = os.path.splitext(data['filename'])[0]
        data['language'] = self.language(data)
        res['source'] = self.source_template.render(data)
        return res

class SourceTemplate(BaseTemplate):
    def get_keywords(self):
        return {'filename': os.path.basename(self.file_path)}


class FilenameTemplate(BaseTemplate):
    pass

class Template(object):
    def __init__(self, id, name, description, file_root, files):
        self.id = id
        self.name = name
        self.description = description
        self.file_root = file_root
        self.files = files
        self.destination_dir = os.getcwd()

    def set_destination(self, dest):
        self.destination_dir = dest

    def set_project_name(self, name):
        self.project = name

    def ready_to_render(self):
        if not self.project:
            return False
        return True

    def get_keywords(self):
        keywords = {'id': self.id,
                'name': self.name,
                'description': self.description,
                'file_root': self.file_root,
                'project': self.project,
                }
        return keywords

    def render(self, template):
        keywords = self.get_keywords()
        return template.render(keywords)

    def write(self):
        for f in self.get_files():
            templates = self.render(f)
            print "Writing:", templates['destination']
            #print templates
            with codecs.open(templates['destination'], encoding='utf-8', mode='w') as dst:
                dst.write(templates['source'])

    def get_files(self):
        for f in self.files:
            source_filename = os.path.join(self.file_root, "templates", f[0])
            source_template = SourceTemplate(source_filename, f[1], self)
            yield source_template

    def apply_templating(self):
        pass

    def __str__(self):
        return "<{template.__class__.__name__} | {template.name} | {template.description}> {template.file_root}".format(template=self)

    @classmethod
    def creator(cls, index):
        stream = file(index, 'r')
        file_root = os.path.dirname(os.path.abspath(index))
        index = yaml.load(stream)
        template = cls(index['id'], index.get('name', 'Untitled'), index.get('description', ''), file_root, index.get('files', []))
        return template

def index_repository():
    for root, dirs, files in os.walk(repo_dir):
        if "index.yaml" in files:
            rep = Template.creator(os.path.join(root, "index.yaml"))
            REPOSITORY[rep.id] = rep

        #print(sum(getsize(join(root, name)) for name in files), end=" ")
        #print("bytes in", len(files), "non-directory files")
        #if 'CVS' in dirs:
        #    dirs.remove('CVS')  # don't visit CVS directories



