r"""
The first name of this package was supposed to be jsontools. But there was another package with that name. So we chose the name jsonpull.
This package is supposed to provide interesting tools for working with JSON.
Currently only has JPrint. JPrint format the output of JSON objects for printing.
We will add better features in the future.
"""
__version__ = '0.0.1'
__all__ = [
    'jprint',
]

__author__ = 'Majid Azizian <azizian.majid@gmail.com>'

import json


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
