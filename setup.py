from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-template-request",
    description="Expose the Datasette request object to custom templates",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-template-request",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-template-request/issues",
        "CI": "https://github.com/simonw/datasette-template-request/actions",
        "Changelog": "https://github.com/simonw/datasette-template-request/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_template_request"],
    entry_points={"datasette": ["template_request = datasette_template_request"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    tests_require=["datasette-template-request[test]"],
    python_requires=">=3.6",
)
