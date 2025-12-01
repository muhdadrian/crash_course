# Plotting a Simple Line Graph

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() #1
ax.plot(squares)

plt.show()


# - we first import the pyplot module. 
# - pyplot module contains a number of functions that generate charts and plots.
# - we create a list called squares to hold the data that we'll plot.
# - we follow another common Matplotlib convention by calling the subplots() function. This function can generate one or more plots in the same figure.
# - the var fig represents entire figure or collection of plots that are generated.
# - the var ax represents a single plot in the figure and is the var we'll use most of the time.
# - we then use the plot()  method, which will try to plot the data it's given in a meaningful way.
# - the function plt.show() opens Matplotlib's viewer and displays the plot.
