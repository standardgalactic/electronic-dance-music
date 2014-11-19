import matplotlib.pyplot as plt
import matplotlib
import numpy as np

plt.figure(figsize=(4,4))
ax = plt.subplot(1, 1, 1)
color = '#999999'
plt.gca().tick_params(axis='x', color=color)
plt.gca().tick_params(axis='y', color=color)
for child in plt.gca().get_children():
    if isinstance(child, matplotlib.spines.Spine):
        child.set_color(color)


grid_number = 7
cm = plt.get_cmap('gist_earth')
ax.set_color_cycle([cm(1.*i/(grid_number)) for i in range(grid_number)])
for i in range(1,grid_number + 1):
    if(i == 3 or i == 5):
        continue
    x = 2 + i * 0.5
    data = np.genfromtxt('grid_{}.dat'.format(i))
    ax.plot((data[:,0] - 2) / 3, data[:,1])
    plt.xlim(0,2)
    ax.set_xlabel("$\sigma$")
    ax.set_ylabel("$h$")
plt.savefig("hills.png", dpi=250)

