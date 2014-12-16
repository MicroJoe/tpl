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

from tpl.template import render_template_comment

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

    import argparse

    parser = argparse.ArgumentParser(description="write on stdout templates.")
    parser.add_argument("TEMPLATE_NAME")
    parser.add_argument("LANGUAGE_NAME")
    parser.add_argument("-p", "--project", dest="project", help="project name")
    parser.add_argument("-a", "--author", dest="author", help="author name")

    args = parser.parse_args()

    context = infer_context()

    if args.project:
        context["project"] = args.project
    if args.author:
        context["author"] = args.author

    res = render_template_comment(sys.argv[1], sys.argv[2], context=context)

    if not res:
        sys.exit(1)

    print(res)


if __name__ == "__main__":
    main()
