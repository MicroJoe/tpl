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
import getpass
from datetime import datetime

from tpl.template import render_template

from tpl import settings


def usage():
    print('usage: tpl <template_name> <language_name>')


def infer_context():
    """Load the context based on current environment.

    Returns:
        A dict containing all the contextual data.

    """

    context = {
        'author': 'my_author',
        'year': datetime.now().year,
        'project': 'my_project'
    }

    try:
        with open(settings.USER_CONFIG) as f:
            conf = json.load(f)
        context['author'] = conf['author']
    except FileNotFoundError:
        print('warning: JSON file ~/.tplrc not found', file=sys.stderr)
        context['author'] = getpass.getuser()

    context['project'] = os.path.basename(os.getcwd())

    return context


def main():

    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    context = infer_context()

    print(render_template(sys.argv[1], sys.argv[2], context=context))


if __name__ == "__main__":
    main()
