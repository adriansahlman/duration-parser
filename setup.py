import re
import os
from setuptools import (
    setup,
    find_packages,
)
from typing import Optional


def find_version(
    fpath: str,
) -> Optional[str]:
    with open(fpath, 'r') as fp:
        match = re.search(
            r'(?<=__version__ = [\'"])([^\'"]+)(?=[\'"])',
            fp.read(),
        )
    if not match:
        return None
    return match.group(1)


root = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(root, 'README.md'), 'r') as fp:
    long_description = fp.read()


version = find_version(os.path.join(root, 'duration_parser/__init__.py'))
if not version:
    raise RuntimeError('could not find version of duration_parser')


setup(
    name='duration-parser',
    version=version,
    description='Duration parser.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/adriansahlman/duration-parser',
    author='Adrian Sahlman',
    author_email='adrian.sahlman@gmail.com',
    license='MIT',
    packages=find_packages(include=('duration_parser', 'duration_parser.*')),
    package_data={'duration_parser': ['py.typed']},
    python_requires='>=3.7',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
    ],
    keywords='duration parse parser parsing',
)
