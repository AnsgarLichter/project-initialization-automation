from multiprocessing.util import is_exiting
from winreg import ExpandEnvironmentStrings
import os
import shutil

import git
from github import Github, GithubException


class Repository:
    README_FILE_NAME = "README.md"

    BRANCH_MAIN = "main"
    REMOTE_ORIGIN = "origin"
    COMMIT_MESSAGE_INITIAL = "Initial commit"

    PUSH_SET_UPSTREAM = "-u"

    def __init__(self, config):
        self.config = config
        self.user = Github(self.config.getAuthToken()).get_user()
        self.repository = None

    def __createLocal(self):
        repositoryPath = self.config.getRepositoriesPath() + '\\' + self.config.getRepositoryName()
        if os.path.exists(repositoryPath):
            print("Directory already existing")
            quit()
        
        repositoryDirectory = os.path.join(self.config.getRepositoriesPath(), self.config.getRepositoryName())
        self.repository = git.Repo.init(repositoryDirectory)

    def __createDefaultReadme(self):
        repositoryPath = self.config.getRepositoriesPath() + '\\' + self.config.getRepositoryName()
        readmePath = repositoryPath + "\\" + Repository.README_FILE_NAME

        with open(readmePath, "w+") as readme:
            readme.write("# " + self.config.getRepositoryName())

    def __createGithub(self):
        gitRepository = self.user.create_repo(self.config.getRepositoryName())
        origin = self.repository.create_remote(Repository.REMOTE_ORIGIN, gitRepository.ssh_url)
        origin.fetch()
    
    def __commitInitial(self):
        self.repository.index.add(Repository.README_FILE_NAME)
        self.repository.index.commit(Repository.COMMIT_MESSAGE_INITIAL)
    
    def __push(self):
        self.repository.git.branch(Repository.BRANCH_MAIN)
        self.repository.git.checkout(Repository.BRANCH_MAIN)
        self.repository.git.push(Repository.PUSH_SET_UPSTREAM, Repository.REMOTE_ORIGIN, Repository.BRANCH_MAIN)

    def isExisting(self):
        if self.user.get_repo(self.config.getRepositoryName()):
            return True
        else:
            return False

    def create(self):
        self.__createLocal()

        self.__createGithub()

        self.__createDefaultReadme()
        self.__commitInitial()
        self.__push()

    def deleteLocal(self):
        repositoryPath = self.config.getRepositoriesPath() + '\\' + self.config.getRepositoryName()

        shutil.rmtree(repositoryPath, ignore_errors=True)
