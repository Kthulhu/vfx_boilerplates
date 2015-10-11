# -*- coding: utf-8 -*-
__author__ = 'fredrik.brannbacka'
import vfxboilerplates as vfxb
import os
import yaml
import codecs
import vfxboilerplates.launguages as languages
import vfxboilerplates.applications as applications
from templating import env, Loader, SourceTemplate

REPOSITORY = {}
repo_dir = os.path.abspath(os.path.join(vfxb.ROOT_DIR, "..", "repository"))


class Template(object):
    def __init__(self, id, name, description, file_root, files, language, application):
        self.id = id
        self.name = name
        self.project = "Untitled"
        self.description = description
        self.file_root = file_root
        self.files = files
        self.destination_dir = os.getcwd()
        self.language = language
        self.application = application()

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
            try:
                os.makedirs(os.path.dirname(templates['destination']))
            except:
                pass
            print "Writing:", templates['destination']
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
        return "<{template.__class__.__name__} | {template.name} | {template.description}> {template.file_root}".format(
            template=self)

    @classmethod
    def creator(cls, index):
        stream = file(index, 'r')
        file_root = os.path.dirname(os.path.abspath(index))
        index = yaml.load(stream)
        template = cls(
            id=index['id'],
            name=index.get('name', 'Untitled'),
            description=index.get('description', ''),
            file_root=file_root,
            files=index.get('files', []),
            language=languages.get(index.get('language', None)),
            application=applications.get(index.get('application', None))
        )
        return template


def index_repository():
    for root, dirs, files in os.walk(repo_dir):
        if "index.yaml" in files:
            rep = Template.creator(os.path.join(root, "index.yaml"))
            REPOSITORY[rep.id] = rep
