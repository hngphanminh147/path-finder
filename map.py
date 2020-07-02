import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

w = 50
h = 50

# Polygons
p1 = [[8, 6], [10, 20], [22, 16]]
p2 = [[27, 17], [33, 15], [35, 31], [27, 31]]
p3 = [[16, 40], [26, 41], [35, 39], [14, 32]]
# Wall
w1 = [[5, 5], [5, 20], [6, 20], [6, 5]]
w2 = [[15, 30], [25, 30], [25, 29], [15, 29]]
w3 = [[37, 40], [38, 40], [38, 20], [37, 20]]

s = (2, 2)
d = (40, 40)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks = np.arange(0, (w + 1) if w > h else (h + 1), 5)
minor_ticks = np.arange(0, (w + 1) if w > h else (h + 1), 1)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

ax.grid(which='major', color='#7f7f7f', linestyle='--')
ax.grid(which='minor', color='#b2b2b2', linestyle=':')

b = [[1, 1], [1, h - 1],[w - 1, h - 1], [w - 1, 1]]
barrier_out = patches.Rectangle((0, 0), w, h, linewidth=1, edgecolor='#7f7f7f', facecolor='#7f7f7f')
barrier_in = patches.Polygon(b, linewidth=1, edgecolor='#ffffff', facecolor='#ffffff')
ax.add_patch(barrier_out)
ax.add_patch(barrier_in)

# start
plt.plot(s[0], s[1], marker='s', color='#ff2100')
# destination
plt.plot(d[0], d[1], marker='s', color='#2600ff')

# barrier
# op1 = plt.Polygon(p1, facecolor='#00ff00')
# ax.add_patch(op1)

# op2 = plt.Polygon(p2, facecolor='#0000ff')
# ax.add_patch(op2)

# op3 = plt.Polygon(p3, facecolor='#ff0000')
# ax.add_patch(op3)

ow1 = plt.Polygon(w1, facecolor='#00ff00')
ax.add_patch(ow1)

ow2 = plt.Polygon(w2, facecolor='#0000ff')
ax.add_patch(ow2)

ow3 = plt.Polygon(w3, facecolor='#ff0000')
ax.add_patch(ow3)

plt.show()