# POSTS API Test Framework using Pytest-BDD and Requests

This test framework is built using pytest-bdd and Requests library to test CRUD operations against Web API's

Requirements:

## Requirements

- Python 3.6+
- Pytest-BDD
- Pytest
- Requests

## Setup
This project requires an up-to-date version of Python 3.
It also uses [pipenv](https://pipenv.readthedocs.io/) to manage packages.

To set up this project on your local machine:
1. Clone it from this GitHub repository.
2. Run `pipenv install` from the command line in the project's root directory.
3. Run `pipenv shell` to activate the virtual environment
4. Install the libraries that are needed for this project
    - Requests, Pytest-BDD, Pytest

pipenv install requests

## Running Tests
The test can be executed by running the command `pytest`

To check for any link errors use the command `flake8`

Alternatively, make command can be used to run the tests i.e 
`make test`

Firstly the flake8 lint command is executed followed by pytest.

The make commands are helpful when we are running on multiple environments  