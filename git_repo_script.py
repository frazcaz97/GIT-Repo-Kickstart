import github
import getpass
import git
import os

def loginToGithub():
    print("GITHUB LOGIN")
    token = getpass.getpass("Access Token: ") #input token without echo to console
    try: #test login is valid
        g = github.Github(token)
        testLogin = g.get_user().login
    except github.GithubException as exception:
        if "401" in str(exception):
            print("Invalid Access Token")
        else:
            print("credential error")
    else:
        createRemoteRepo(g)

def createRemoteRepo(login):
    print("New repository name must not conflict with current local/remote repository names")
    repoName = input("Input new repository name: ")

    if " " in repoName: #format repo name for github
        print("there is white space")
        repoName = repoName.replace(" ", "-")
        
    if checkDirectoryName(repoName) is True: #local repo name is unique
        try: #check new repo name is valid
            checkDirectoryName(repoName)
            login.get_user().create_repo(repoName,private=True)
        except github.GithubException as exception:
            if "422" in str(exception):
                print("Remote repository name already exists")
                createRemoteRepo(login)
            else:
                print("Remote repository error")
    else:
        print("Local repository name already exists")
        createRemoteRepo(login)
        
def checkDirectoryName(name):
    dir = os.path.join("D:\\","code",name) #local repo file path
    if not os.path.exists(dir): #file path is valid
        return True
    else:
        return False


def createLocalRepo(name):
    pass

loginToGithub()

