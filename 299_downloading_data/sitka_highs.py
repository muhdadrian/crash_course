import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f: #1
    reader = csv.reader(f) #2
    header_row = next(reader) #3
    print(header_row)