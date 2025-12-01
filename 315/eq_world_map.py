# Building a World Map

import json

from plotly.graph_objs import Scattergeo, Layout #1
from plotly import offline

filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

# Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats)] #2
my_layout = Layout(title='Global Earthquakes') #3

fig = {'data': data, 'layout': my_layout} #4
offline.plot(fig, filename='global_earthquakes.html')

'''
A Different Way of Specifying Chart Data
In the current chart above, the data list is defined in one line:

data = [Scattergeo(lon=lons, lat=lats)]

It's one of the simplest ways to define the data for a chart in Plotly. But, it's not the best way
when you want to customize the presentation. Here's an equivalent way to define the data for the 
current chart:

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
}]
'''