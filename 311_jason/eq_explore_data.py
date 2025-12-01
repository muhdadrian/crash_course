# Examining JSON Data

import json

# Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) #1

readable_file = 'data/readable_eq_data.json' #2
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4) #3

# the result will go to data folder