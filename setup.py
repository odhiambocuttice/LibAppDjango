import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='LibraryApp',
    version='1.0.9',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple django library app ',
    long_description=README,
    author='kevin',
    author_email='kevin@kev.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',

    ],
    install_requires=[
        'Django==2.2.2',
        'pytest-django==3.5.0',
        'django-pytest==0.2.0',
        'djangorestframework==3.9.4'
        
    ],
    scripts=[
        "bin/locallibrary_app"
    ],
)