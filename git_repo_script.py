import github
import getpass
import git
import os

print("GITHUB LOGIN")
token = getpass.getpass("Access Token: ")   #input token without echo to console
filePath = "D://code/" #file path for git repo directories

def loginToGithub(token):
    try:   #test login is valid
        githubUser = github.Github(token)
        testLogin = githubUser.get_user().login
    except github.GithubException as exception:
        if "401" in str(exception):
            print("Invalid Access Token")
            loginToGithub()
        else:
            print("credential error")
            input()
    else:   #login is valid, continue script
        createRemoteRepo(githubUser)

def createRemoteRepo(login):
    print("New repository name must not conflict with current local/remote repository names")
    repoName = input("New repository name: ")

    if " " in repoName:   #format repo name for github
        repoName = repoName.replace(" ", "-")
        
    if checkLocalName(repoName) is True:   #local repo name is unique
        try:   #check new repo name is valid
            login.get_user().create_repo(repoName,private=True)
            print("Github remote repository initialised")
            createLocalRepo(repoName)
        except github.GithubException as exception:
            if "422" in str(exception):
                print("Remote repository name already exists")
                createRemoteRepo(login)
            else:
                print("Remote repository error")
                input()
    else:
        print("Local repository name already exists")
        createRemoteRepo(login)
        
def checkLocalName(name):
    dirP = os.path.join(filePath,name)
    if not os.path.exists(dirP):   #file path is valid
        return True
    else:
        return False

def createLocalRepo(name):
    try:    #initialise the local repo 
        repoDir = os.path.join(filePath,name)
        init = git.Repo.init(repoDir)
        print("Git local repository initialised")
        createRemoteLink(repoDir,name)
    except Exception as exception:
        print("Local repository error")
        input()

def createRemoteLink(repoDir,name):
    try:    #create the remote link
        g = github.Github(token)
        url = "https://github.com/" + g.get_user().login + "/" + g.get_user().get_repo(name).name + ".git"
        git.Repo(repoDir).create_remote("origin",url)
        print("Git remote origin set")
        print("setup complete")
    except Exception as exception:
        print(exception)

loginToGithub(token)


