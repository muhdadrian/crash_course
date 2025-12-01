# Extracting and Reading Data

import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures from this file.
    highs = [] #1
    for row in reader: #2
        high = int(row[5]) #3
        highs.append(high)

print(highs)