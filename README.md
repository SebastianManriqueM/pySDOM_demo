# NREL SDOM (Storage Deployment Optimization Model) Demo

This repository demonstrates how to set up and use the Python-based version of NREL's Storage Deployment Optimization Model (SDOM).

## Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
      - [Install uv and Create a Virtual Environment](#install-uv-and-create-a-virtual-environment)
      - [Install SDOM Python Package and Logging](#install-sdom-python-package-and-logging)
- [Usage](#usage)

## Introduction

SDOM is a tool for optimizing storage deployment. This guide will help you get started with the Python implementation.

## Prerequisites

- Python installed on your system.
- Access to the command line (PowerShell or similar).

## Installation

### Install uv and Create a Virtual Environment

1. Install `uv`, a Python manager for virtual environments and packages. Follow the instructions at [uv on PyPI](https://pypi.org/project/uv/).
2. Create a new virtual environment named `.venv`:

            ```powershell
            uv venv .venv
            ```

            This command creates a Python virtual environment in the `.venv` directory.

### Install SDOM Python Package and Logging

1. Activate your virtual environment and install the SDOM package:

            ```powershell
            uv pip install sdom
            ```

            This will also install all required dependencies.

2. Install the Logging package:

            ```powershell
            uv pip install logging
            ```

3. Verify your environment by listing installed packages:

            ```powershell
            uv pip list
            ```

            You should see output similar to:

            ```powershell
            Package         Version
            --------------- -----------
            logging         0.4.9.6
            numpy           2.3.2
            pandas          2.3.1
            ply             3.11
            pyomo           6.9.3
            python-dateutil 2.9.0.post0
            pytz            2025.2
            sdom            0.0.3
            six             1.17.0
            tzdata          2025.2
            ```

## Usage

- Refer to the `demo.py` script in this repository for an example of how to use SDOM.
- Do not forget to include in you project the compiled code of cbc solver and point the path when executing "run_solver()" function. Currently python version of SDOM only runs with this solver.
- The demo uses the CBC solver. To use it, copy the `Solver` folder and specify the path to `cbc.exe` in your configuration.

