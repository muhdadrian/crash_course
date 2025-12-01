'''
Using a Colormap
A colormap is a series of colors in a gradient that moves from a starting to an ending color. You
use colormaps in visualizations to emphasize a pattern in the data. For example, you might make
low values a light color and high values a darker color.

The pyplot module includes a set of built-in colormaps. To use one of these colormaps, you need
to specify how pyplot should assign a color to each point in the data set. Here’s how to assign
each point a color based on its y-value:
'''

import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) # update this line

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()

'''
You can see all the colormaps available in pyplot at https://matplotlib.org/; go to Examples, 
scroll down to Color, and click Colormap reference.
'''