# Pyclense

An Object-Oriented, Data Cleaning Toolkit for Python.

Pyclense is a beginner-friendly Python library designed to simplify and automate essential data cleaning tasks. Built with an object-oriented structure, it allows you to clean, transform, and export datasets using reusable, modular components.

Unlike simple script-based solutions, Pyclense uses *Inheritance*, *Polymorphism*, and *Composition* to create a stable and scalable environment for your data cleaning workflows.

---

## Badges

[![PyPI version](https://badge.fury.io/py/pyclense.svg)](https://badge.fury.io/py/pyclense)  
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyclense)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Key Features

1. *Quick Missing Data Fixer*  
   Spot and fill in blank or empty values in your dataset. You can replace them with mean, median, mode, or a default value — Pyclense handles the logic for you.

2. *Duplicate Remover*  
   Easily detect and remove repeated rows or entries. It highlights duplicates and lets you clean them with a single command.

3. *Format Standardizer*  
   Unify inconsistent formatting in your dataset — such as transforming dates into one format (e.g., MM/DD/YYYY) or removing emojis and special symbols from text fields.

4. *Easy Data Preview and Export*  
   Preview your data before and after cleaning using built-in table views. Export the cleaned dataset to CSV or Excel, including an auto-generated cleaning summary.

---

## Installation

Install Pyclense via PyPI:

pip install pyclense
`

### From Source

git clone https://github.com/Athea-123/Pyclense.git
cd Pyclense
pip install -e .

---

## Quick Start

from pyclense.cleaners import DuplicateCleaner, MissingDataCleaner
from pyclense.pipeline import CleaningPipeline
import pandas as pd

df = pd.read_csv("raw_data.csv")

pipeline = CleaningPipeline(initial_cleaner=MissingDataCleaner())
pipeline.add_step(DuplicateCleaner)
cleaned_df = pipeline.run(df)

cleaned_df.to_csv("cleaned_output.csv", index=False)

---

## Core Modules Explained

Pyclense is built on a modular, object-oriented architecture. Each cleaner is a subclass of BaseCleaner and is designed to perform a *single responsibility* within the cleaning process.

### Orchestrators

#### *CleaningPipeline*

The CleaningPipeline acts as the central manager of the cleaning workflow. It:

* Accepts an initial cleaner
* Allows additional cleaning steps to be added
* Passes the dataset sequentially through each step
* Produces a final cleaned output

*Example:*

pipeline = CleaningPipeline(initial_cleaner)
pipeline.add_step(DuplicateCleaner)
pipeline.run(df)
