from package.config import Config
from package.repository import Repository

from github import GithubException

config = Config()
repository = Repository(config)

try:
    repository.create()
    print("Successfully created GitHub repository {}!".format(config.getRepositoryName()))

except GithubException:
        repository.deleteLocal()
        print("Unfortunately the repository couldn't be created")