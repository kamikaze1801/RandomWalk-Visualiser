import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Making a RandomWalk
rw = RandomWalk(100_000)
rw.fill_walk()

#Plotting points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize = (15,9))
point_numbers = range(rw.num_points)

#Adding the color gradient and plotting the walk
ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors= 'none', s = 5)
ax.set_aspect('equal')

#Starting and ending points of the points
ax.scatter(0, 0, c = "green", edgecolors= "none", s = 100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors= "none", s = 100)

#Removing Axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
