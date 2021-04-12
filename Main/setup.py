import setuptools

with open("README.md", r) as fh:
    long_description = fh.read()

setuptools.setup(
    name="versuschsstand-NICOLAS-AMIR-HAKIMI",
    version= "0.0.1",
    author="Nicholas Tan Jerome",
    author_email="ntj@imko.de",
    description="package for the testing platform of newly designed sensor from IMKO GmbH",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages()
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires= '>=3.6',
)