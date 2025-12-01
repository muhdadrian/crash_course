'''
Defining Custom Colors
To change the color of the points, pass c to scatter() with the name of a color to use in quotation
marks, as shown here:

ax.scatter(x_values, y_values, c='red', s=10)
'''

import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c='red', s=10) # update this line

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()

'''

'''