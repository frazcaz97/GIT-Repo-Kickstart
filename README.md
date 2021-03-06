# GIT local/remote kickstart script

## Overview
This script:
  - Initialises a new remote repository
  - clones remote repository to local
  - Sets the remote url

## Requirements
-Git installed on your local machine

-A Github account with a personal access token created (see Github documentation: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

-The Following Python modules:
  - pyGithub
  - gitPython

## File Path

The script requires a file path to clone the remote repo to

```python
print("GITHUB LOGIN")
token = input("Access Token: ")
filePath = "/home/User/Documents/git-repos/" #file path for git repo directories
```

change the filePath variable to suit your file location
