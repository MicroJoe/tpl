# coding: utf-8
#
# TPL
# A simple template-based file creator.
# 
# Copyright (C) Romain PORTE (MicroJoe)

import sys
from os import path

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

from comments import load_language, comment_multiline

def render_template(template_name, language_name):
    templates_path = path.join(path.dirname(__file__), 'templates')

    context = {
        'author': 'Romain PORTE (MicroJoe)',
        'year': 2014,
        'project': 'TPL'
    }

    env = Environment(loader=FileSystemLoader(templates_path))

    try:
        template = env.get_template('{}.txt'.format(template_name))
    except TemplateNotFound:
        print('error: template file {} not found'.format(template_name))
        sys.exit(1)

    result = template.render(context)

    try:
        return comment_multiline(result, load_language(language_name))
    except FileNotFoundError:
        print('error: JSON description file for language {} not found'.format(
            language_name)
        )
        sys.exit(1)

def usage():
    print('usage: tpl <template_name> <language_name>')

if __name__ == '__main__':

    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    print(render_template(sys.argv[1], sys.argv[2]))
