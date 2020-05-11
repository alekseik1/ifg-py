import setuptools
import re

meta_file = open("ifg/metadata.py").read()
metadata = dict(re.findall(r"__([a-z]+)__\s*=\s*'([^']+)'", meta_file))


def get_long_description():
    with open('README.md', 'r') as fh:
        long_description = fh.read()
        return long_description


setuptools.setup(
    name='ifg',
    version=metadata['version'],
    author='Aleksei Kozharin',
    author_email='1alekseik1@gmail.com',
    description='Package for numerical calculations of ideal Fermi gas',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/alekseik1/ifg-py',
    packages=setuptools.find_packages(),
    setup_requires=['fdint', 'numpy', 'scipy', ],
    install_requires=[
        'fdint',
        'scipy',
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=2.7',
)
