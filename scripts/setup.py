from setuptools import setup, find_packages

setup(
    name='rpmdepsearch',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'rpmdepsearch = rpmdepsearch.main'
        ]
    },
    install_requires=[
        'python3'
    ],
)