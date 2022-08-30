import os
import argparse

from package import constants
from package.config import Config
from package.repository_factory import RepositoryFactory, RepositoryFactoryException

from github import Github, GithubException

parser = argparse.ArgumentParser()
parser.add_argument("repository_name", help="enter the name of the repository")
args = parser.parse_args()

config = Config()
github = Github(config.get_authentication_token())
repositoryFactory = RepositoryFactory(github)

repository_name = args.repository_name

try:
    repository = repositoryFactory.create_repository(repository_name, config.get_repositories_path())

    readme_path = os.path.join(repository.working_dir, f"README.{constants.MARKDOWN_FILE_EXTENSION}")
    with open(readme_path, "w+") as readme:
        readme.write(f"{constants.MARKDOWN_HEADING_1} {repository_name}\n")

    repository.git.add(readme.name)
    repository.git.commit(constants.COMMIT_OPTION_MESSAGE, constants.COMMIT_MESSAGE_INITIAL)

    repository.git.branch(constants.BRANCH_NAME_MAIN)
    repository.git.push(constants.PUSH_OPTION_SET_UPSTREAM, constants.REMOTE_ORIGIN, constants.BRANCH_NAME_MAIN)

    print(f"Repository {repository_name} successfully created")
except RepositoryFactoryException as repository_factory_exception:
    print(f"The repository {repository_name} couldn't be created: {repository_factory_exception.message}")

except GithubException as github_exception:
    print(f"An error occurred communicating with the Github API: {github_exception}")