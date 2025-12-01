# Rolling Two Dice

from plotly.graph_objs import Bar, Layout # add this one
from plotly import offline # add this one also

from dice import Dice

# Create a D6
dice_1 = Dice() #add this one
dice_2 = Dice() # add this one too

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = dice_1.roll() + dice_2.roll() #1
    results.append(result)

# Analyze the results.
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides #2
for value in range(1, max_result + 1): #3
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1} #4
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

