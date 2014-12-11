# TPL, a simple template-based file creator

Write template-based source code on stdout.

## Description

This program is used in order to generate source code based on templates. Since
these templates are mostly licencing ones, there is a language-based comment
system in order to separate the text template from the language-specific
comment format.

You can add your own templates and languages using text files.

## Usage

Example usage:

    :::console
    $ tpl
    usage: tpl <template_name> <language_name>
    $ tpl agpl c
    /*
     * ...
     */

## Adding your own templates

You can add a template by creating a text file in the `templates/` directory.
The name of the file must end with `.txt` and will be used as the template
name (for example `my_template.txt`).

This text file contains text and fields surrounded by double braces, like
`{{ year }}` ; fields will be replaced by their value during generation.

Example template:

    :::text
    This file is part of {{ project }}.
    Copyright (C) {{ year }} {{ author }}.

## Adding your own language support

You can add support for a specific language by creating a text file under the
`languages/` directory. This file is under JSON format and so must have a
`.json` extension (like `python.json`).

This JSON file describes the way comments are handled in the language:

    :::javascript
    {
        "language": "your_language_name",
        "format": {
            "inline": {
                "before": "inline_comment_open_string",
                "after": "inline_comment_close_string",
            },
            "multiline": {
                "first": "multiline_comment_open_string",
                "while": "multiline_comment_newline_string",
                "final": "multiline_comment_close_string"
            }
        }
    }

You can take a look at the provided languages files in order to create your
own.

## Copyright

This program is brought to you under GNU General Public License v3+. For
further informations please read the COPYING file.
