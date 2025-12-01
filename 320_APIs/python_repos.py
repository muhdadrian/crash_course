# Processing an API Response

import requests #1

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars' #2
headers = {'Accept': 'application/vnd.github.v3+json'} #3
r = requests.get(url, headers=headers) #4
print(f"Status code: {r.status_code}") #5

# Store API response in a var.
response_dict = r.json() #6

# Process results.
print(response_dict.keys())

'''
search in browser for the data:
https://api.github.com/search/repositories?q=language:python&sort=stars

#6 - we use json() method to convert the info to a Python dictionary, as the API returns the info in
JSON format.
'''