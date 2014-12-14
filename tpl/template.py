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


def render_template_text(template_name, context):
    """Render a template to raw text.

    Args:
        template_name (string) : name of the template (without .txt extension)
        context (dict) : context to be rendered inside the template

    Returns:
        A string containing the generated text.

    """
    env = Environment(loader=FileSystemLoader(settings.TEMPLATES_DIR))

    try:
        template = env.get_template('{}.txt'.format(template_name))
    except TemplateNotFound:
        print('error: template file {} not found inside {}'
              .format(template_name, settings.TEMPLATES_DIR), file=sys.stderr)
        return

    return template.render(context)


def render_template_comment(template_name, language_name, context):
    """Render a template to comment.

    Args:
        template_name (string) : name of the template (without .txt extension)
        language_name (string) : name of the language (without .json extension)
        context (dict) : context to be rendered inside the template

    """

    result = render_template_text(template_name, context)
    lang = load_language(language_name, settings.LANGUAGES_DIR)

    if result and lang:
        return comment_multiline(result, lang)
