#Arpit Patel
#The following code is to get the number of commits from the Git User in the Repo
import requests
import json


# get repositories
def get_repos(user_name):
    response = requests.get(f'https://api.github.com/users/{user_name}/repos')
    res = json.loads(response.text)
    return res


# get commits
def get_commits(user_name, repo_name):
    response = requests.get(f'https://api.github.com/repos/{user_name}/{repo_name}/commits')
    res = json.loads(response.text)
    return res


def get_git_info(user_name):
    repo_res = get_repos(user_name)
    if isinstance(repo_res, list):
        result = ''
        for repo in repo_res:
            repo_name = repo['name']
            commit_num = len(get_commits(user_name, repo_name))
            result += f'Repo: {repo_name} Number of commits: {commit_num}'
        return result
    else:
        raise ValueError(f'Can not find this people {user_name}')


def main():
    user_name = input('Please enter github user name: ')
    get_git_info(user_name)


if __name__ == '__main__':
    get_git_info('richkempinski')
    # main()