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

from tpl.comments import load_language, comment_multiline


ROOT_DIR = path.dirname(__file__)
TEMPLATES_DIR = path.join(ROOT_DIR, 'templates')
LANGUAGES_DIR = path.join(ROOT_DIR, 'languages')


def render_template(template_name, language_name):

    context = {
        'author': 'Romain PORTE (MicroJoe)',
        'year': 2014,
        'project': 'TPL'
    }

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    try:
        template = env.get_template('{}.txt'.format(template_name))
    except TemplateNotFound:
        print('error: template file {} not found inside {}'
              .format(template_name, templates_path))
        sys.exit(1)

    result = template.render(context)

    try:
        lang = load_language(language_name, LANGUAGES_DIR)
        return comment_multiline(result, lang)
    except FileNotFoundError:
        print('error: JSON description file for language {} not found inside {}'
              .format(language_name, LANGUAGES_DIR))
        sys.exit(1)


def usage():
    print('usage: tpl <template_name> <language_name>')


def run(*args, **kwargs):
    print(render_template(sys.argv[1], sys.argv[2]))
