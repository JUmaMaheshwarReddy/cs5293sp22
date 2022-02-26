from setuptools import setup, find_packages

setup(
        name='project1',
        version='1.0',
        author='Mahesh',
        author_email='umamaheshwar00@gmail.com',
        packages=find_packages(exclude=('tests','docs'))
        )
