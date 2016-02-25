from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    DESCRIPTION = readme.read()

setup(
    name="boids",
    version="0.1.0",
    packages=find_packages(exclude=["*tests", ]),
    package_data={'boids':['*.yml']},
    test_suite='nose.collector',
    tests_require=['mock', 'nose', 'pyyaml'],
    scripts=['scripts/boids'],
    install_requires=['argparse', 'numpy', 'matplotlib'],
    author="Joshua D. Foster",
    author_email="joshua.foster@ucl.ac.uk",
    description=["Command line tool to generate an animation of a" +
                 "flock of boids."],
    long_description=DESCRIPTION,
    license="MIT",
    keywords="boids animation vectors",
    url="https://github.com/jdfoster/boids",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"
    ]
)
