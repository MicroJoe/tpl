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

"""Module used for comments generation."""

from os import path
import json
import sys

from tpl import settings


def load_language(language_name, languages_dir):
    """Load a language description JSON file.

    Args:
        language_name (string) : name of the language (without .json extension)
        languages_dir (string) : directory to look in for the JSON file

    Returns:
        The loaded language dict, or None if loading failed.

    """
    uri = path.join(languages_dir, '{}.json'.format(language_name))

    try:
        with open(uri) as f:
            language = json.load(f)
    except FileNotFoundError:
        print('error: JSON description file for language {} not found inside {}'
              .format(language_name, settings.LANGUAGES_DIR),
              file=sys.stderr)
        return

    return language


def comment_inline(text, language):
    """Generate a comment for the specified language on one line.

    Args:
        text (string) : text to put inside the comment
        language (dict) : language description dictionnary

    Returns:
        A string containing the formatted comment.

    """
    result = '{}{}{}\n'.format(
        language['format']['inline']['before'],
        text,
        language['format']['inline']['after']
    )
    return result


def comment_multiline(text, language):
    """Generate a comment for the specified language on multiple lines.

    Args:
        text (string) : text to put inside the comment
        language (dict) : language description dictionnary

    Returns:
        A string containing the formatted comment.

    """
    middle = '\n'.join([
        '{}{}'.format(
            language['format']['multiline']['while'],
            line
        ) for line in text.splitlines()])

    return '{}\n{}\n{}\n'.format(
        language['format']['multiline']['first'],
        middle,
        language['format']['multiline']['final']
    )
