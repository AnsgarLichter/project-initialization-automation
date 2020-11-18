import os
from github import Github
import git

#TODO: read from config file
repositoriesPath = r'C:\Users\Ansgar\Development\repositories'

#TODO: get from console
repositoryName = 'test2'

repositoryPath = repositoriesPath + '\\' + repositoryName
if os.path.exists(repositoryPath):
    print("Directory already existing")
    quit()

# Create Local Repository
repositoryDirectory = os.path.join(repositoriesPath, repositoryName)
repository = git.Repo.init(repositoryDirectory)

readmePath = repositoryPath + "\\" + "README.md"
with open( readmePath, "w+") as readme:
    readme.write("# " + repositoryName)

#TODO: read from config file
user = Github("fc30637b7f3edda0e62b641da075b6e42fa2a11e").get_user()
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