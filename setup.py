from setuptools import setup, find_packages

setup(
    name="Pyclense",
    version="0.1.0",
    author="Athea Jane Budlong, Kate Avancena, Belle Margareth Jacobo, Sariba Abdula ",
    author_email= "budlong.atheajane@gmail.com, kateavanmarfe@gmail.com, jacobo.jynobellemargareth@gmail.com, abdula.sariba28@gmail.com",
    description="A simple, user-friendly Python library for basic data cleaning tasks.",
    long_description=open("README.md").read() if open("README.md").read() else "",
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/Pyclense", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "numpy",
        "openpyxl",  # Required for the new Excel support features
    ],
)

