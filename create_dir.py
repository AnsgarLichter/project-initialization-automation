import os
from github import Github
import git

#TODO: read from config file
repositoriesPath = r'C:\Users\Ansgar\Development\repositories'

#TODO: get from console
repositoryName = 'test'

repositoryPath = repositoriesPath + '\\' + repositoryName
if os.path.exists(repositoryPath):
    print("Directory already existing")
    quit()

# Create Local Repository
repositoryDirectory = os.path.join(repositoriesPath, repositoryName)
repository = git.Repo.init(repositoryDirectory)

readmePath = repositoryPath + "\\" + "README.md"
readme = open( readmePath, "w+")
readme.write("# " + repositoryName)
readme.close()

#TODO: read from config file
user = Github("").get_user()
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