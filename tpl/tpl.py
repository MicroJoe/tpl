# coding: utf-8
#
# TPL
# A simple template-based file creator.
#
# Copyright (C) Romain PORTE (MicroJoe)

import sys
import os
import json
from datetime import datetime

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

from tpl.comments import load_language, comment_multiline


ROOT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')
LANGUAGES_DIR = os.path.join(ROOT_DIR, 'languages')

USER_CONFIG = os.path.expanduser('~/.tplrc')


context = {
    'author': 'my_author',
    'year': datetime.now().year,
    'project': 'my_project'
}


def render_template(template_name, language_name):

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

    try:
        template = env.get_template('{}.txt'.format(template_name))
    except TemplateNotFound:
        print('error: template file {} not found inside {}'
              .format(template_name, TEMPLATES_DIR), file=sys.stderr)
        sys.exit(1)

    result = template.render(context)

    try:
        lang = load_language(language_name, LANGUAGES_DIR)
        return comment_multiline(result, lang)
    except FileNotFoundError:
        print('error: JSON description file for language {} not found inside {}'
              .format(language_name, LANGUAGES_DIR),
              file=sys.stderr)
        sys.exit(2)


def usage():
    print('usage: tpl <template_name> <language_name>')


def run(*args, **kwargs):

    try:
        with open(USER_CONFIG) as f:
            conf = json.load(f)
        context['author'] = conf['author']
    except FileNotFoundError:
        print('warning: JSON file ~/.tplrc not found', file=sys.stderr)
    context['project'] = os.path.basename(os.getcwd())

    print(render_template(sys.argv[1], sys.argv[2]))
