from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='author name',
    author_email='author@email',
    url='https://github.com/repo',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
