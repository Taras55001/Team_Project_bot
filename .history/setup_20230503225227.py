from setuptools import setup, find_packages
with open('README.md', 'r') as f:
long_description = f.read()
with open('requirements.txt') as f:
requirements = f.read().splitlines()
setup(
name='MemoMind',
version='1.0.0',
author='Code Cobras',
author_email='john.doe@example.com',
description='My package description',
long_description=long_description,
packages=find_packages(),
install_requires=requirements,
)
