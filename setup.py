# It is a module that help us to build and distribute python packages
# Project details(contains information of package,name,version & dependencies) can be found using setup.py file
# setup.py file can be accessed/triggered from requirements.txt by >> -e. in the script.

from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e.'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

    if HYPEN_E_DOT in requirements: # removing -e. from requirements.txt so that it is not read along with pandas and throw error
        requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name = 'Fault Detection',
    version = '0.0.1',
    author= 'Aman',
    author_mail= 'akaman0877@gmail.com',
    install_requirements= get_requirements('requirements.txt'),
    packages= find_packages() # identifies package and stores it.
)