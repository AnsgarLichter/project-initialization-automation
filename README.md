# Project Initialization Automation

## What does the script?

This script automates the process of creating a new repository. Therefore, the following steps are executed:

 1. The script asks you to enter the name of the new repository
 2. A new local folder is created in the config's path and a Github repository is Initialized
 3. A new git repository is created in your account
 4. A readme is created with the repository's name as title in the local folder.
 5. The changes are committed.
 6. The changes are pushed to the main branch to synchronize the local and the upstream repository.

[PyGithub](https://pygithub.readthedocs.io/) is used to handle operations regarding Github.

## Get started

 1. Clone the repository
 2. Create your GitHub authorization token and grant all permissions regarding repositories
 3. Add your GitHub authorization token in `params.txt`
 4. Add your local path where all your repositories shoud be saved in `params.txt`
 5. Install all required dependencies executing `pip install -r requirements.txt`
 6. Execute the script running `python main.py`

## Contact

If you have found a bug or want to request a new feature please feel free top open a new issue.