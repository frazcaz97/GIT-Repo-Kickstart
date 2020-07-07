import github
import getpass

print("Github login")
token = getpass.getpass("Access Token")

g = github.Github(token)

for repo in g.get_user().get_repos():
    print(repo.name)
