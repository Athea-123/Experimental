# Pyclense

*An Object-Oriented, Data Cleaning Toolkit for Python.*
Pyclense is a….

Unlike simple script-based solutions, Pyclense uses Inheritance, Polymorphism, and Composition to create a stable and scalable environment for your data cleaning workflows.

## Key Features

1.  *Quick Missing Data Fixer*: Spot and fill in blank or empty spots in your data. You just tell it what to do (like replace blanks with averages or a default word), and it handles it automatically. 
2.  *Duplicate Remover*: Easily find and delete repeated rows in your dataset. It scans your file, shows you the duplicates, and lets you remove them with one command, helping keep your data clean and organized.
3.  *Format Standardizer*: Helps make sure all your data looks consistent, like changing dates to the same style (e.g., MM/DD/YYYY). It also removes special characters, such as emojis and non-standard symbols, from text fields to ensure the data is clean and plain.
4.  *Easy Data Preview and Export*: Before and after cleaning, you can preview your data in a simple table view. Then, export the cleaned version to common formats like CSV or Excel, with a summary of what was changed, so you can see the results right away.

## Installation

You can install Pyclense directly from PyPI:

pip install pyclense
### From Source
git clone https://github.com/Athea-123/Pyclense.git
cd Pyclense
pip install -e .

## Quick Start
## Core Modules Explained

Pyclense is built

### Orchestrators

#### CleaningPipeline

It acts as a manager that contains a list of cleaning steps. It accepts an initial cleaner and passes the data through each added step sequentially.

pipeline = CleaningPipeline(initial_cleaner)
pipeline.add_step(DuplicateCleaner)
pipeline.run()
### 