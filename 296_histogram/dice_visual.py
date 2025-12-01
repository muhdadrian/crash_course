# Making a Histogram

from plotly.graph_objs import Bar, Layout # add this one
from plotly import offline # add this one also

from dice import Dice

# Create a D6
dice = Dice()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, dice.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, dice.num_sides + 1)) #1
data = [Bar(x=x_values, y=frequencies)] #2

x_axis_config = {'title': 'Result'} #3
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config) #4
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html') #5

# Plotly has made the chart interactive: hover your cursor over any bar in the chart, and you'll
# see the associated data.