import json

class Config:
    repositoriesPath = ""
    githubAuthToken = ""

    def __init__(self):
        with open("params.txt") as f:
            parameters = json.load(f)

        self.repositoriesPath = parameters["repositoriesPath"]
        self.githubAuthToken = parameters["githubAuthToken"]
        self.repositoryName = input("Please enter your repository name: ")

    def getRepositoriesPath(self):
        
        return self.repositoriesPath

    def getAuthToken(self):
        return self.githubAuthToken

    def getRepositoryName(self):
        return self.repositoryName