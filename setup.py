from setuptools import find_packages, setup
from typing import List

def get_requirements(filename:str) -> List[str]:
    '''
    This function will return the list of Python libraries required
    '''
    requirements = []
    with open(filename) as f_obj:
        requirements = f_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements


setup(
    name = 'mlproject',
    version='0.0.1',
    author='Nimisha',
    author_email='nimisha.jadav7@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)