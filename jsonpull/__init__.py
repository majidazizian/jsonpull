"""
The first name of this package was supposed to be jsontools. But there was another package with that name. So we chose the name jsonpull.
This package is supposed to provide interesting tools for working with JSON.
Currently only has JPrint. JPrint format the output of JSON objects for printing.
We will add better features in the future.
"""

from .__version__ import __version__
from . import jprint

__version__ = '0.0.1'
__all__ = [
    'jprint',
]

__author__ = 'Majid Azizian <azizian.majid@gmail.com>'

