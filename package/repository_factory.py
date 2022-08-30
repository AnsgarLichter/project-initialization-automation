import os
import git

from package import constants

from github import Github, GithubException

class RepositoryFactory:
    def __init__(self, github: Github) -> None:
        self.__github = github
        
        self.__user = self.__github.get_user()
    
    def get_repository(self, repository_name) -> git.Repo:
        return git.Repo(repository_name)
    
    def create_repository(self, repository_name: str, repository_base_path: str) -> git.Repo:
        self.__validate(repository_name, repository_base_path)

        repository_path = os.path.join(repository_base_path, repository_name)
        repository = git.Repo.init(repository_path)
        github_repository = self.__user.create_repo(repository_name)

        repository.create_remote(constants.REMOTE_ORIGIN, github_repository.ssh_url)
        return repository

    def __validate(self, repository_name: str, repository_base_path: str) -> None:
        repository_path = os.path.join(repository_base_path, repository_name)

        if os.path.exists(repository_path):
            raise RepositoryFactoryException("Local directory is already existing")
        elif self.is_repository_existing_for_current_user(repository_name):
            raise RepositoryFactoryException("Remote repository is already existing")
    
    def is_repository_existing_for_current_user(self, repository_name) -> bool:        
        try:
            self.__user.get_repo(repository_name)
            return True
        except GithubException as github_exception:
            if github_exception.status != 404:
                raise github_exception
            
            return False
        
class RepositoryFactoryException(Exception):

    def __init__(self, message):
        super().__init__()
        self.__message = message

    @property
    def message(self):
        return self.__message

    def __str__(self):
        return "{message}"
