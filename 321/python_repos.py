# Working with the Response Dictionary

import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a var.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}") #1

# Explore info about the repositories.
repo_dicts = response_dict['items'] #2
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dicts = repo_dicts[0] #3
print(f"\nKeys: {len(repo_dicts)}") #4
for key in sorted(repo_dicts.keys()): #5
    print(key)
