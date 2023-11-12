from setuptools import setup, find_packages

with open('.\\requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='paavana_dsss_hw2',
    version='1.0.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'math_quiz=math_quiz:main',
        ],
    },
    # Other metadata like author, description, etc.
)
