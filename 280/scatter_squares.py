'''
Add a title, label the axes, and make sure all the text is large enough to read:
'''

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200) #1

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

'''
At #1 we call scatter() and use the s argument to set the size of the dots used to draw the graph.
'''