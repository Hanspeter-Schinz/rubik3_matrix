from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="rubik3_matrix",
    version="0.0.1",
    author="Hanspeter Schinz",
    author_email="hanspeter.schinz@gmx.ch",
    description="A package to find solutions for a 3x3x3 rubiks cube",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/hanspeter-schinz/rubik3_matrix/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)