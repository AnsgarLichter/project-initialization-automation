import os
from github import Github
import git
import json

with open("params.txt") as f:
    parameters = json.load(f)

repositoriesPath = parameters["repositoriesPath"]
githubAuthToken = parameters["githubAuthToken"]

repositoryName = input("Please enter your repository name: ")

repositoryPath = repositoriesPath + '\\' + repositoryName
if os.path.exists(repositoryPath):
    print("Directory already existing")
    quit()


repositoryDirectory = os.path.join(repositoriesPath, repositoryName)
repository = git.Repo.init(repositoryDirectory)

readmePath = repositoryPath + "\\" + "README.md"
with open( readmePath, "w+") as readme:
    readme.write("# " + repositoryName)


user = Github(githubAuthToken).get_user()
gitRepository = user.create_repo(repositoryName)

origin = repository.create_remote('origin', gitRepository.ssh_url)
origin.fetch()


repository.index.add("README.md")
repository.index.commit("Created repository with an empty README")

repository.git.branch("main")
repository.git.checkout("main")
repository.git.push("-u", "origin", "main")

if user.get_repo(repositoryName):
    print("Successfully created repository " + repositoryName + " with url " + gitRepository.ssh_url)
else:
    print("Repository not created")