import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="dasci",
    version="0.1",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    long_description=read('README.md'),
)