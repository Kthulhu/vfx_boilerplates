from vfxboilerplates.launguages import Language
import jinja2

HEADER =\
r"""/*
* file: {{filename}}
*/"""

HEADER_GUARD=\
r"""
#ifndef {{project | upper}}_H
#define {{project | upper}}_H"""

class Cpp(Language):
    def __init__(self, keywords):
        super(Cpp, self).__init__(keywords)

    @property
    def header(self):
        print self.keywords
        header = HEADER
        if self.keywords['filename'].endswith(".h"):
            header += HEADER_GUARD
        template = jinja2.Template(header)
        return template.render(self.keywords)

    @property
    def footer(self):
        footer = ""
        if self.keywords['filename'].endswith(".h"):
            footer = r"#endif /* {{project | upper}}_H */"
        template = jinja2.Template(footer)
        return template.render(self.keywords)


