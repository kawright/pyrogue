import os
from setuptools import setup

"""
This module configures setuptools, which will allow us to register this
package with `pypi`, as well as generate distributables for our package and
upload them to `pypi`.
"""

def read_readme() -> str:
    """Read the contents of `README.md` and return it as a `str."""

    return open(os.path.join(os.path.dirname(__file__), "README.md")).read()

setup(
    name="pyrogue",
    version="0.1.0",
    description="Wrapper for the `pygame` libary which provides a simple " + \
        "API for creating roguelike or other ASCII-tile based games.",
    long_description=read_readme(),
    author="Kristoffer A. Wright",
    author_email="kris.al.wright@gmail.com",
    url="http://kriswrightdev.com/pyrogue",
    py_modules=[
        "pyrogue"
    ],
    license="MIT",
    platforms="any"
)