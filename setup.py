from setuptools import setup, find_packages

# Safely read README
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_desc = f.read()
except FileNotFoundError:
    long_desc = ""

setup(
    name="Pyclense",
    version="0.1.1",
    author="Group 7",
    description="A simple, user-friendly Python library for basic data cleaning tasks.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/Athea-123/Pyclense",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas>=2.0.0',
        'openpyxl>=3.1.0'
    ],
    entry_points={
        "console_scripts": [
            "pyclense = pyclense.cli:main",
        ]
    },
)
