from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> list[str]:
    """
    this function will return the list of requirement
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [request.replace("\n", "") for request in requirements]

    return requirements


setup(
    name="HR-dataset-ML-project",
    version="0.0.1",
    author="anuj kumar",
    author_email="anujmahlawat16@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
