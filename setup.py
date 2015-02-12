import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='indigo-django',
    version='0.1',
    packages=['indigo'],
    include_package_data=True,
    description='A simple Django app providing UCL Indigo layouts and styles',
    long_description=README,
    url='http://www.ucl.ac.uk/indigo/',
    author='Helen Sherwood-Taylor',
    author_email='h.sherwood-taylor@ucl.ac.uk',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
