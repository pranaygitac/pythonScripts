

# To create repo#####################################3

import requests
import os

def create_github_repo(token, repo_name, description):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    data = {
        'name': repo_name,
        'description': description,
        'private': False,  # Set to True if you want a private repository
    }

    api_url = 'https://api.github.com/user/repos'

    response = requests.post(api_url, json=data, headers=headers)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully!")
    else:
        print(f"Failed to create repository. Status code: {response.status_code}")
        print(response.json())

def delete_github_repo(token, repo_owner, repo_name):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}'

    response = requests.delete(api_url, headers=headers)

    if response.status_code == 204:
        print(f"Repository '{repo_owner}/{repo_name}' deleted successfully!")
    else:
        print(f"Failed to delete repository. Status code: {response.status_code}")
        print(response.json())        

# Replace these values with your GitHub personal access token, repository name, and description
github_token = os.environ.get("git_token") #export git_token=ghp_7kzVJjE5DrDSqnAssdvdsvdsvhwycx41ndDq
repository_name = input("pls eneter reponame: ")
repository_owner = input("pls eneter repo_owner_username: ")
repository_description = 'This is a new repository created using GitHub API'

print("do you want to create or delete a repo")
user_input = input("create/delete : ")

if user_input == "create":
        create_github_repo(github_token, repository_name, repository_description)
elif user_input == "delete":
        delete_github_repo(github_token, repository_owner, repository_name)
else:
        print("Invalid choice. Please enter either create or delete.")







# def ask_question():
#     print("Which option do you prefer?")
#     print("1. Option A")
#     print("2. Option B")

#     user_input = input("Enter your choice (1 or 2): ")

    

