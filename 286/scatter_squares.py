'''
Saving Your Plots Automatically
If you want your program to automatically save the plot to a file, you can replace the call to
plt.show() with a call to plt.savefig():

plt.savefig('squares_plot.png', bbox_inches='tight')

The first argument is a filename for the plot image, which will be saved in the same directory as
scatter_squares.py. The second argument trims extra whitespace from the plot. If you want the
extra whitespace around the plot, just omit this argument.
'''

import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight') # update this line

'''

'''