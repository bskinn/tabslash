from pathlib import Path
from setuptools import find_packages, setup


with (Path(".") / "src" / "tabslash" / "version.py").open() as f:
    exec(f.read())

NAME = "tabslash"

setup(
    name=NAME,
    version=__version__,
    description="Toy project for testing autodoc on pos-only args",
    long_description="",
#    url="https://github.com/bskinn/sphobjinv",
    license="MIT License",
    author="Brian Skinn",
    author_email="bskinn@alum.mit.edu",
    packages=find_packages("src"),
    package_dir={"": "src"},
    provides=["tabslash"],
    python_requires=">=3.5",
#    requires=["attrs (>=17.4)", "certifi", "fuzzywuzzy (>=0.3)", "jsonschema (>=2.0)"],
#    install_requires=["attrs>=17.4", "certifi", "fuzzywuzzy>=0.3", "jsonschema>=2.0"],
    classifiers=[
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
#        "Environment :: Console",
#        "Framework :: Sphinx",
#        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
 #       "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
    ],
#    entry_points={"console_scripts": ["sphobjinv = sphobjinv.cmdline:main"]},
)
