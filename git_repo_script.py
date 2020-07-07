import github
import getpass

def loginToGithub():
    print("Github login")
    token = getpass.getpass("Access Token")
    try:
        g = github.Github(token)
        testLogin = g.get_user().login
        print(testLogin)

        createGithubRepo()
        
    except:
        print("Invalid access token")

def createGithubRepo():
    pass

loginToGithub()
