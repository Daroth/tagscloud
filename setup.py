from setuptools import setup, find_packages

README = open('README.md').read().strip()
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: '
]

setup(
    name="tagscloud",
    version="0.0.1",
    packages=find_packages(),
    author='Daroth',
    author_email='daroth@braindead.fr',
    description='Tagscloud library',
    license='Beerware',
    keywords='tags cloud',
    url=''
)
