from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e."

def get_requirements(file_paths:str)->List[str]:
    #this fuction will return the list of reqirements
    
    requirements=[]
    with open(file_paths) as file_obj:
        requirements=file_obj.readline()
        reqirrequirementsements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
        return requirements







setup(
    name="MLPROJECT1",
    version="0.0.1",
    author="Ankit",
    author_email="singhankite101@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)


