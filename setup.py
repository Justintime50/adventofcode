import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'black == 24.*',
    'flake8 == 7.*',
    'isort == 5.*',
    'pytest == 8.*',
    'pytest-cov == 5.*',
]

# NOTE: This repository is not intended to be distributed as a package and as such is not setup as one correctly

setuptools.setup(
    name='adventofcode',
    version='0.1.0',
    description='An Advent calendar of coding challenges.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/adventofcode',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.10, <4',
)
