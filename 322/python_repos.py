import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a var.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore info about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dicts = repo_dicts[0]

print("\nSelected information about first repository:")
print(f"Name: {repo_dicts['name']}") #1
print(f"Owner: {repo_dicts['owner']['login']}") #2
print(f"Stars: {repo_dicts['stargazers_count']}") #3
print(f"Repository: {repo_dicts['html_url']}")
print(f"Created: {repo_dicts['created_at']}") #4
print(f"Updated: {repo_dicts['updated_at']}") #5
print(f"Description: {repo_dicts['description']}")
