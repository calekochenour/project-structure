# Getting started with open and reproducible scientific programming projects.

One key step to open and reproducible science to provide rigorous organization of all project material. Not just for someone else to use, but also for you, if and when you return to the project after some time and/or when the project complexity increases.

This repository provides a Python script to create the following project structure within the current working directory:

```
.
├── 01-code-scripts/
├── 02-raw-data/
├── 03-processed-data/
├── 04-graphics-outputs/
└── 05-papers-writings/
```

The project structure was inspired by an [article](https://www.earthdatascience.org/courses/intro-to-earth-data-science/open-reproducible-science/get-started-open-reproducible-science/best-practices-for-organizing-open-reproducible-science/) from the University of Colorado Boulder Earth Lab.

In addition to the folder structure, this repository provides:

* `Makefile` to automate folder creation and deletion
* `environment.yml` to create the Conda environment

Complementary resources:

* [Medium article]()
* [Video tutorial]()

## Prerequisites

To run this project locally, you will need:

* Conda ([Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/))

To run this project in a web browser, click the icon below to launch the project with Binder:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/calekochenour/project-structure/main)

Binder will open a Jupyter Notebook in the current web browser. Click "New" and select "Terminal" to open a terminal in the project folder.

## Instructions

### Create and Activate Conda Environment

From the terminal, you can create and activate the project Conda environment.

Create environment:

```bash
$ conda env create -f environment.yml
```

Activate environment:

```bash
$ conda activate reproducible-science
```

### Run the Code

From the terminal (locally or within Binder), you can run the code and create the project structure.

Create structure:

```bash
$ make create
```

Delete structure (folders only):
```bash
make clean
```

## Contents

This repository contains all files required to create the project structure.

### `create_folders.py`

Python script used to create the project structure.

### `environment.yml`

Contains the information required to create the Conda environment.

### `Makefile`

Contains instructions to execute the code.

## Folder Descriptions

The structure created during the code execution contains folders for all stages of the scientific workflow.

### `01-code-scripts/`

Contains all code required to run analyses.

### `02-raw-data/`

Contains all original/unprocessed data.

### `03-processed-data/`

Contains all processed/created data.

### `04-graphics-outputs/`

Contains all figures.

### `05-papers-writings/`

Contains all paper/report files.
