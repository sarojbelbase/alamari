from os import path

from setuptools import find_packages, setup

about = {}
with open('alamari/__about__.py') as fp:
    exec(fp.read(), about)


if path.isfile('README.md'):
    long_description = open('README.md').read()
else:
    long_description = 'See https://github.com/sidbelbase/alamari#readme'


if __name__ == '__main__':
    setup(
        name=about['__package_name__'],
        version=about['__version__'],
        author=about['__author__'],
        author_email=about['__author_email__'],
        description=about['__description__'],
        url=about['__url__'],
        license='MIT',
        packages=find_packages(exclude=[
            '*.__pycache__', 'venv', '.github']),
        long_description=long_description,
        long_description_content_type='text/markdown',
        install_requires=['arrow', 'nepali-datetime',
                          'nepali-roman', 'python-dateutil', 'requests'],
        setup_requires=[],
        keywords=['nepali-utils', 'made-in-nepal', 'nepal', 'nepali-developer',
                  'nepali-package', 'pluralize', 'devanagari', 'roman', 'nepal-time', 'helper-functions', 'utilities'],
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires='>=3.6',
    )
