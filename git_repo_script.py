import github
import getpass
import git
import os

filePath = "D://code/" #local repo's directory

def loginToGithub():
    print("GITHUB LOGIN")
    token = getpass.getpass("Access Token: ")   #input token without echo to console
    try:   #test login is valid
        g = github.Github(token)
        testLogin = g.get_user().login
    except github.GithubException as exception:
        if "401" in str(exception):
            print("Invalid Access Token")
            loginToGithub()
        else:
            print("credential error")
            input()
    else:
        createRemoteRepo(g)

def createRemoteRepo(login):
    print("New repository name must not conflict with current local/remote repository names")
    repoName = input("Input new repository name: ")

    if " " in repoName:   #format repo name for github
        repoName = repoName.replace(" ", "-")
        
    if checkLocalName(repoName) is True:   #local repo name is unique
        try:   #check new repo name is valid
            login.get_user().create_repo(repoName,private=True)
            createLocalRepo(repoName)
        except github.GithubException as exception:
            if "422" in str(exception):
                print("Remote repository name already exists")
                createRemoteRepo(login)
            else:
                print("Remote repository error")
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
        #remote = repoDir.create_remote("origin", remoteURL)
    except Exception as exception:
        print("Local repository error")

loginToGithub()


