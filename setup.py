from setuptools import setup, find_packages


def get_requirements(file_path="requirements.txt"):
    """
    This function reads the requirements from a file and returns a list of packages.
    :param file_path: Path to the requirements file
    :return: List of required packages
    """
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
            
    return requirements


# Setup configuration for the package
setup(
name="mlproject",
version="0.0.1",
author="Ardavan",
author_email="ardavan.sh007@gmail.com",
packages=find_packages(),  # Automatically find packages in the current directory
install_requires=get_requirements()

)