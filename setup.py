import os
from setuptools import setup, find_packages


PACKAGE_NAME = 'jsonpull'
DESCRIPTION = 'create a formatted string of the Python JSON object'
URL = 'https://github.com/majidazizian/jsonpull'
AUTHOR = 'Majid Azizian'
EMAIL = 'azizian.majid@gmail.com.com'
VERSION = '0.1.0'


REQUIRES_PYTHON = '>=3.6.0'

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements("./requirement.txt", session=False)

try:
    REQUIRED = [str(ir.req) for ir in install_reqs]
except:
    REQUIRED = [str(ir.requirement) for ir in install_reqs]

EXTRAS = {}

#
pwd = os.path.abspath(os.path.dirname(__file__))

# load readme
try:
    with open('README.md', encoding='utf-8') as f:
        readme = f.read()
except FileNotFoundError:
    readme = "No README.md exists"

# load license
try:
    with open('LICENSE.md', encoding='utf-8') as f:
        license = f.read()
except FileNotFoundError:
    license = "No LICENCE yet"

# load package VERSION
try:
    about = {}
    pkg = PACKAGE_NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(pwd, pkg, '__version__.py')) as f:
        exec(f.read(), about)
    VERSION = about['__version__']
except FileNotFoundError:
    VERSION = '0.1.0'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=readme,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license=license,
    python_requires=REQUIRES_PYTHON,
    #packages=find_packages(exclude=('./algoanalysis/tests', './algoanalysis/docs')),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
