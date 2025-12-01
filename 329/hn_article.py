# The Hacker News API

'''
https://news.ycombinator.com/
- to explore how to use API calls on other sites
'''

'''
https://hacker-news.firebaseio.com/v0/item/19155826.json

{"by":"jimktrains2","descendants":221,"id":19155826,"kids":[19156572,19158857,19156773,19157251,
19156415,19159820,19157154,19156385,19156489,19158522,19156755,19156974,19158319,19157034,
19156935,19158935,19157531,19158638,19156466,19156758,19156565,19156498,19156335,19156041,19156704,
19159047,19159127,19156217,19156375,19157945],"score":728,"time":1550085414,"title":"Nasa’s Mars 
Rover Opportunity Concludes a 15-Year Mission","type":"story","url":"https://www.nytimes.com/2019/
02/13/science/mars-opportunity-rover-dead.html"}

- it's a dictionary
- run the URL through json.dump() method, to explore the kind of info 
'''

import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)