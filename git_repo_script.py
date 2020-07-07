import github
import getpass

def loginToGithub():
    print("GITHUB LOGIN")
    token = getpass.getpass("Access Token: ") #input token without echo to console
    try: #test login is valid
        g = github.Github(token)
        testLogin = g.get_user().login
        print(testLogin)
    except:
        print("Invalid Access Token")
    else:
        createGithubRepo(g)

def createGithubRepo(login):
    repoName = input("Input new repository name: ")
    validName = True
    if " " in repoName: #format repo name for github
        print("there is white space")
        repoName = repoName.replace(" ", "-")

    for repo in login.get_user().get_repos(): #check repo name is valid
        print(repo.name)
        if repoName == repo.name:
            validName = False
            break;
            
    if validName is True: # try to init the repo
        print("this name has not been used before")

        try:
            pass
        except:
            pass
    else: #ask user to enter a new name
        print("repository name already exists, please try again")
        createGithubRepo(login)
                
            
    #init new repo if name is valid

#loginToGithub()
g = github.Github("")
createGithubRepo(g)
