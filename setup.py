import setuptools
from ifg_py import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='ifg_py',
    version=__version__,
    author='Aleksei Kozharin',
    author_email='1alekseik1@gmail.com',
    description='Package for numerical calculations of ideal Fermi gas',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alekseik1/ifg-py',
    packages=setuptools.find_packages(),
    install_requires=[
        'fdint',
        'scipy',
        'numpy',
        'pandas'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

