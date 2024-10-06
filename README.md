# Software Development Engineer in Test - Home Assignment

This repository contains the home assignment for the `Software Development Engineer in Test` role. It includes the implementation of **Task #1** and **Task #2**.

## Task #1 - Coding Assignment

The first task involves creating a solution to validate the maximum number of releases per Sprint. The implementation is located in `assignment/task_1/ReleasePlanner.py`.

Since the task requires reading from and writing to files, the following files [`releases.txt`, `solution.txt`] are provided in the `resources` folder.

This project utilizes Python 3.12 and **Pytest** for testing. Dependency management is handled by **Poetry**, a tool for packaging and managing Python project dependencies. More details about Poetry can be found at: [https://python-poetry.org/](https://python-poetry.org/)

### Installation

To install Poetry, run the following command:

`pip install poetry`

After installing Poetry, it will automatically apply the project settings from the configuration files [`pyproject.toml`, `poetry.lock`].

### Running the Project

You can run the coding task using this command:

`poetry run python assignment/task_1/ReleasePlanner.py`

### Running Tests

To run the tests, use the following command:

`poetry run pytest -v`

## Task #2 - Strategic Proposal

The second task involves strategic thinking about increasing adoption rates for integration and performance tests among software engineers. This task has been implemented in **Markdown** (MD) format for easy readability and is included as a document in the repository.
