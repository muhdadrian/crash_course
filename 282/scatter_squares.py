'''
Calculating Data Automatically
Writing lists by hand can be inefficient, especially when we have many points. Rather than passing
our points in a list, let's use a loop in Python to do the calculations for us.
'''

# Here's how this would look with 1000 points:

import matplotlib.pyplot as plt

x_values = range(1, 1000) #1
y_values = [x**2 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10) #2

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000]) #3

plt.show()

'''

'''