'''
You can also define custom colors using the RGB color model. To define a color, pass the c
argument a tuple with three decimal values (one each for red, green, and blue in that order),
using values between 0 and 1. For example, the following line creates a plot with light-green
dots:

ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

Values closer to 0 produce dark colors, and values closer to 1 produce lighter colors.

BUT, YOU'LL GET A WARNING FOR USING THIS KIND OF CUSTOM COLORS.
'''

import matplotlib.pyplot as plt

x_values = range(1, 1000)
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10) # update this line

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()

'''

'''