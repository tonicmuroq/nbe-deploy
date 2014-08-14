# coding: utf-8

from setuptools import setup, find_packages


setup(
    name='nbe-deploy',
    version='0.1',
    author='tonic',
    zip_safe=False,
    author_email='tonic@wolege.ca',
    description='deploy tool set for NBE',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts':['nbe=nbe.commands:nbecommands'],
    },
    install_requires=[
        'click>=2.0',
        'requests>=2.2.1',
        'PyYAML',
    ],
)
