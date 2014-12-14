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

"""Contains all the useful constants of the program."""

import os


ROOT_DIR = os.path.dirname(__file__)
TEMPLATES_DIR = os.path.join(ROOT_DIR, 'templates')
LANGUAGES_DIR = os.path.join(ROOT_DIR, 'languages')

USER_CONFIG = os.path.expanduser('~/.tplrc')
