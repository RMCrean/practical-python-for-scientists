from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = "TODO"
LONG_DESCRIPTION = """
TODO
"""

setup(
    name="py-for-science",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Rory Crean",
    author_email="rory.crean@kemi.uu.se", 
    url="https://github.com/RMCrean/practical-python-for-scientists",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "notebook",
        "scikit-learn",
        "scipy",
        "numpy",
        "pandas",
        "lxml",
        "matplotlib",
        "plotly",
        "kaleido",
    ],
    extras_require={
        "dev": ["pytest", "setuptools", "mkdocs", "mkdocs-material", "mkdocstrings", "mkdocs-jupyter"],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
