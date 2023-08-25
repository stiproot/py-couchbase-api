from setuptools import setup, find_packages
import os

name = "pyxi_couchbase_api"
description = "A basic restful service that acts as a Couchbase proxy."
author = "Simon Stipcich"
author_email = "stipcich.simon@gmail.com"
url = "https://github.com/stiproot/py-couchbase-api"
license = "MIT"
keywords = ["python", "package", "couchbase", "beta"]
version = "0.0.1"
install_requires = [
    "environs==9.5.0",
    "fastapi==0.101.1",
    "pyxi_couchbase_client==0.0.1",
]
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    packages=find_packages("src"),
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    keywords=keywords,
    install_requires=install_requires,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
)
