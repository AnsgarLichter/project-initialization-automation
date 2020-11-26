from github import Github
import git
import os

class Repository:
    def __init__(self, config):
        self.config = config
        self.user = Github(self.config.getAuthToken()).get_user()
        self.createLocalRepository()
        self.createReadme()
        self.createGithubRepository()

    def createLocalRepository(self):
        repositoryPath = self.config.getRepositoriesPath() + '\\' + self.config.getRepositoryName()
        if os.path.exists(repositoryPath):
            print("Directory already existing")
            quit()
        
        repositoryDirectory = os.path.join(self.config.getRepositoriesPath(), self.config.getRepositoryName())
        self.repository = git.Repo.init(repositoryDirectory)

    def createReadme(self):
        repositoryPath = self.config.getRepositoriesPath() + '\\' + self.config.getRepositoryName()
        readmePath = repositoryPath + "\\" + "README.md"

        with open(readmePath, "w+") as readme:
            readme.write("# " + self.config.getRepositoryName())

    def createGithubRepository(self):
        gitRepository = self.user.create_repo(self.config.getRepositoryName())
        origin = self.repository.create_remote('origin', gitRepository.ssh_url)
        origin.fetch()


        self.repository.index.add("README.md")
        self.repository.index.commit("Created repository with an empty README")

        self.repository.git.branch("main")
        self.repository.git.checkout("main")
        self.repository.git.push("-u", "origin", "main")

    def isExisting(self):
        if self.user.get_repo(self.config.getRepositoryName()):
            return True
        else:
            return False