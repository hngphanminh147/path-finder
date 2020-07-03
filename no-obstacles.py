import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import traverse

w = 20
h = 20

# Obstacles
p1 = [[8, 6], [10, 20], [22, 16]]
p2 = [[27, 17], [33, 15], [35, 31], [27, 31]]
p3 = [[16, 40], [26, 41], [35, 39], [14, 32]]
# Wall

s = (2, 2)
d = (18, 17)

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

cost = -1
path = []

# No obstacles
[path, cost] = traverse.traverse(s, d, b, [])

if cost != -1:
    for p in path:
        plt.plot(p[0], p[1], marker='s', color='#ffff00')

# start
plt.plot(s[0], s[1], marker='s', color='#ff2100')
# destination
plt.plot(d[0], d[1], marker='s', color='#2600ff')

plt.show()