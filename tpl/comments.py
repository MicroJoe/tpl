import json

def load_language(language_name):
    uri = './languages/{}.json'.format(language_name)

    with open(uri) as f:
        language = json.load(f)

    return language


def comment_inline(text, language):
    result = '{}{}{}\n'.format(
        language['format']['inline']['before'],
        text,
        language['format']['inline']['after']
    )
    return result

def comment_multiline(text, language):
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
