from distutils.core import setup


setup(
    name='tpl',
    version='0.1.1',

    url='http://microjoe.eu/',

    author='Romain Porte',
    author_email='microjoe@mailoo.org',

    packages=['tpl'],

    include_package_data=True,
    package_data={'tpl': ['templates/*.txt', 'languages/*.json']},


    scripts=['bin/tpl'],

    install_requires=[
        'jinja2',
    ]
)
