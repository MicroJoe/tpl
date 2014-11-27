from distutils.core import setup


setup(
    name='tpl',
    version='0.1.0',

    url='http://microjoe.eu/',

    author='Romain Porte',
    author_email='microjoe@mailoo.org',

    packages=['tpl'],
    include_package_data=True,

    scripts=['bin/tpl'],

    install_requires=[
        'jinja2',
    ]
)
