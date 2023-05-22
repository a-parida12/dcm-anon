# CONTRIBUTION

In this project we use python >=3.8 and poetry for package management, fork your own version and clone it to the local and setup your environment in the following steps

- setup a virtual environment called `.venv` and activate it.
- install poetry

```pip install poetry```

- Once poetry is installed you can install all dependencies by using 

```poetry install```

- Next please install pre-commit in the local 

```pre-commit install```

- Always use commitizen for making commits, the git workflow would be 

1. ```git add <filename>```
2. ```cz commit```
choose the appropriate commit type from the list shown in the terminal and commit accordingly
3. ```git push```
