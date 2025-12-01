# Rolling Dice of Different Sizes

from plotly.graph_objs import Bar, Layout # add this one
from plotly import offline # add this one also

from dice import Dice

# Create a D6 and a D10
dice_1 = Dice()
dice_2 = Dice(10) #1

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times', #2
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

