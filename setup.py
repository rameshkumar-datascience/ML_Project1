from setuptools import setup,find_packages
from typing import List

    
#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Ramesh-Kumar"
DESCRIPTION="This is my first ML project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description:
    return this function is going to return a list which conatain name 
    of libraries mentioned in requirements.txt file
    """
    
    with open(REQUIREMENT_FILE_NAME,'r') as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #wherever it find __init__ it return all those folder names
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())