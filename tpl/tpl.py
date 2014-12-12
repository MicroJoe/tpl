# coding: utf-8

# This file is part of tpl.
# Copyright (C) 2014 Romain 'MicroJoe' PORTE.
#
# tpl is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# tpl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with tpl. If not, see <http://www.gnu.org/licenses/>.

"""Main module of the program."""

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

