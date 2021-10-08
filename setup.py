import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'black',
    'coveralls == 3.*',
    'flake8',
    'isort',
    'pytest == 6.*',
    'pytest-cov == 2.*',
]

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
    entry_points={
        'console_scripts': [
            'adventofcode=github_archive.cli:main',
        ],
    },
    python_requires='>=3.7',
)
