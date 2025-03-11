from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    Get the requirements from the file
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
        
    return requirements
    

setup(
    name= 'ML_Project',
    version= '0.0.1',
    author= 'Simran Malik',
    author_email= 'simran.07malik@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)