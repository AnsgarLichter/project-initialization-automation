# Project Initialization Automation

## What does the script?

This script automates the process of creating a new repository. Therefore, the following steps are executed:

 1. Start the script with your repository name as the first argument
 2. It validates if there is already a local repository or a Github repository. If this is the case the script will show an error message.
 3. A new initial repository is created in your Github account
 4. A new local repository is initialized in your repository base path (config)
 5. A readme is created with the repository's name as title.
 6. The changes are committed.
 7. The changes are pushed to the main branch to synchronize the local and the upstream repository.

[PyGithub](https://pygithub.readthedocs.io/) is used to handle operations regarding Github.

## Get started

 1. Clone the repository
 2. Create your GitHub authorization token and grant all permissions regarding repositories
 3. Rename the `params_example.txt` to `params.txt`
 4. Add your GitHub authorization token in `params.txt`
 5. Add your local path where all your repositories shoud be saved in `params.txt`
 6. Install all required dependencies executing `pip install -r requirements.txt`
 7. Execute the script running `python main.py`

## Contact

If you have found a bug or want to request a new feature please feel free top open a new issue.
