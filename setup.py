from pkg_resources import Requirement
from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    pass

# Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.1",
AUTHOR="Akshaj Piri"
DESCRIPTION="This is a ML Project."
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: this function is goint to return list of requirement mention in requirement
    """


    with open (REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)
