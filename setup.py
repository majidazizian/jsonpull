import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jsonpull", # Replace with your own username
    version="0.0.1",
    author="Majid Azizian",
    author_email="azizian.majid@gmail.com.com",
    description="create a formatted string of the Python JSON object",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/majidazizian/jsonpull",
    packages=setuptools.find_packages(),
    install_requires = [],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)