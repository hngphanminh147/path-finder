# #from stackoverflow
# import matplotlib.pyplot as plt
# import numpy as np

# plt.ion()
# for i in range(5):
#     y = np.random.random([10,1])
#     plt.plot(y)
#     plt.draw()
#     plt.pause(0.1)
    # plt.clf()

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 6*np.pi, 100)
# y = np.sin(x)

# # You probably won't need this if you're embedding things in a tkinter plot...
# plt.ion()

# fig = plt.figure()
# ax = fig.add_subplot(111)
# line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

# for phase in np.linspace(0, 10*np.pi, 500):
#     line1.set_ydata(np.sin(x + phase))
#     fig.canvas.draw()
#     fig.canvas.flush_events()