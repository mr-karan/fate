from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import io
import os
import sys

import fate

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='fate',
    version=fate.__version__,
    url='http://github.com/mr-karan/fate/',
    license='The MIT License',
    author='Karan Sharma',
    tests_require=['pytest'],
    install_requires=['prompt-toolkit>=0.57',
'pyaml==15.8.2',
'Pygments==2.1',
'pyperclip==1.5.26',
'PyYAML==3.11',
'requests==2.9.1',
'six==1.10.0',
'wcwidth==0.1.6',
'wheel==0.24.0',],
    cmdclass={'test': PyTest},
    author_email='karansharma1295@gmail.com',
    description='Browse FontAwesome icons on your command line shell',
    long_description=long_description,
    packages=['fate'],
    include_package_data=True,
    platforms='any',
    test_suite='fate.test.test_fate',
    classifiers = [
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Text Processing :: Fonts',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)