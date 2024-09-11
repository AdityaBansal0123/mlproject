# this is used to make your projects as package on pypi
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(filename):
    with open(filename, "r") as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

setup(
    name= 'mlproject',
    version='0.0.1',
    author='Aditya',
    author_email = 'bansaladitya048@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)


