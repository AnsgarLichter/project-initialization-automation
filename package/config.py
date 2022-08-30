import json

class Config:
    
    PARAMETER_PATH_TO_REPOSITORIES = "repositoriesPath"
    PARAMETER_GITHUB_AUTHENTICATION_TOKEN = "githubAuthToken"


    def __init__(self):
        with open("params.txt") as f:
            parameters = json.load(f)

        self.repositoriesPath = parameters[Config.PARAMETER_PATH_TO_REPOSITORIES]
        self.githubAuthToken = parameters[Config.PARAMETER_GITHUB_AUTHENTICATION_TOKEN]

    def get_repositories_path(self) -> str:        
        return self.repositoriesPath

    def get_authentication_token(self) -> str:
        return self.githubAuthToken