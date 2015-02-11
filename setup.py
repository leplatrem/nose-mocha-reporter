#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Python packaging."""
import os

from setuptools import setup


#: Absolute path to directory containing setup.py file.
here = os.path.abspath(os.path.dirname(__file__))


NAME = 'nose-mocha-reporter'
DESCRIPTION = ''
README = open(os.path.join(here, 'README.rst')).read()
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
AUTHOR = u'Mathieu Leplatre'
EMAIL = 'contact@mathieu-leplatre.info'
LICENSE = 'WTFPL'
URL = ''
CLASSIFIERS = [
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    # Add your classifiers here from
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
]
KEYWORDS = [
    '',
]
PACKAGES = [NAME.replace('-', '_')]
REQUIREMENTS = [
    'setuptools',
]
ENTRY_POINTS = {
    'nose.plugins.0.10': [
        'mocha-reporter = nose_mocha_reporter:MochaReporterPlugin'
    ]
}
TEST_REQUIREMENTS = []
CMDCLASS = {}
SETUP_REQUIREMENTS = [
    'setuptools'
]


if __name__ == '__main__':  # Do not run setup() when we import this module.
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=README,
        classifiers=CLASSIFIERS,
        keywords=' '.join(KEYWORDS),
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        install_requires=REQUIREMENTS,
        entry_points=ENTRY_POINTS,
        tests_require=TEST_REQUIREMENTS,
        cmdclass=CMDCLASS,
        setup_requires=SETUP_REQUIREMENTS,
    )