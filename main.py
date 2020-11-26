from package.config import Config
from package.repository import Repository


if __name__ == '__main__':
    config = Config()
    repository = Repository(config)

    #TODO: Cleanup created files if repository creation failed
    #TODO: Create Readme for the repository itself

    if repository.isExisting():
        print("Successfully created GitHub repository {}!".format(config.getRepositoryName()))
    else:
        print("Unfortunately the repository couldn't be created")