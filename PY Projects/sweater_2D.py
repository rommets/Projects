import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots()
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

body = patches.Rectangle((0.36, 0.31), 0.3, 0.45, linewidth=1, edgecolor='black', facecolor='darkblue')
ax.add_patch(body)
sleeve_left = patches.Polygon([(0.36, 0.76),(0.29,0.45),(0.29,0.45),(0.36,0.45) ],closed=True, linewidth=1, edgecolor='black', facecolor='darkblue')
sleeve_right = patches.Polygon([(0.66,0.76),(0.74,0.45),(0.74, 0.45), (0.66,0.45)], closed=False,linewidth=1, edgecolor='black', facecolor='darkblue')
ax.add_patch(sleeve_left)
ax.add_patch(sleeve_right)

collar = patches.Ellipse((0.51, 0.77),0.12,0.09, linewidth=1, edgecolor='black', facecolor='black')
ax.add_patch(collar)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

plt.title("Your Sweater",fontsize=12,fontweight="black",color="darkgreen",pad=0.0001,loc="center")
plt.show()
