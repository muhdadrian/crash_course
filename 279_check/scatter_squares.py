'''
To plot a single point, use the scatter() method. Pass the single (x, y) values of the point of
interest to scatter() to plot those values:
'''

import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-pastel')
fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()