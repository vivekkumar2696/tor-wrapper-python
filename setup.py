from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='bizarre',
    version='1.0.0',
    description='A python wrapper for tor to browse sites anonymously',
    url='git@github.com:vivekkumar2696/tor-wrapper-python.git',
    author='Vivek Kumar',
    author_email='kumar.vivek2696@gmail.com',
    license='unlicense',
    packages=['bizarre'],
    zip_safe=False,
    install_requires=required
)