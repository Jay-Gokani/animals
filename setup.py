# Contains data to build and distribute Python packages
# pip can instead be used to search PyPi to find, download, extract and install the package

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='animals',
    version='0.1.0',
    description='Sample package to demonstrate an example Python project structure',
    long_description=readme,
    author='Jay Gokani',
    author_email='email@email.com',
    url='https://github.com/Jay-Gokani/animals',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)