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

"""Module used for template formatting."""

import sys
import json

from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateNotFound

from tpl.comments import load_language, comment_multiline
from tpl import settings


def render_template(template_name, language_name, context):
    """Render a template to comment.

    Args:
        template_name (string) : name of the template (without .txt extension)
        language_name (string) : name of the language (without .json extension)
        context (dict) : context to be rendered inside the template

    """

    env = Environment(loader=FileSystemLoader(settings.TEMPLATES_DIR))

    try:
        template = env.get_template('{}.txt'.format(template_name))
    except TemplateNotFound:
        print('error: template file {} not found inside {}'
              .format(template_name, settings.TEMPLATES_DIR), file=sys.stderr)
        sys.exit(1)

    result = template.render(context)

    try:
        lang = load_language(language_name, settings.LANGUAGES_DIR)
        return comment_multiline(result, lang)
    except FileNotFoundError:
        print('error: JSON description file for language {} not found inside {}'
              .format(language_name, settings.LANGUAGES_DIR),
              file=sys.stderr)
        sys.exit(2)
