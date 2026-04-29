import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 4)
ax.set_aspect('equal')
ax.axis('off')

# Drawing the "Cup" (a simple trapezoid)
cup_x = [-1, 1, 0.8, -0.8, -1]
cup_y = [1.5, 1.5, 0, 0, 1.5]
ax.plot(cup_x, cup_y, color='tan', linewidth=4)
ax.fill(cup_x, cup_y, color='#FFE4C4', alpha=0.5)

# Ice cream flavor data: (Color, initial position)
flavors = [
    {'color': '#ffb3ba', 'label': 'Strawberry'},
    {'color': '#baffc9', 'label': 'Mint'},
    {'color': '#ffdfba', 'label': 'Orange'},
    {'color': '#bae1ff', 'label': 'Blueberry'},
    {'color': '#6f4e37', 'label': 'Chocolate'}
]

# Create circles for each flavor
circles = []
for f in flavors:
    circle = plt.Circle((0, 2), 0.5, color=f['color'], ec='black', lw=1)
    ax.add_patch(circle)
    circles.append(circle)

# Animation function
def update(frame):
    for i, circle in enumerate(circles):
        # Create a swirling/bouncing motion using sine and cosine
        # Each flavor gets a slightly different offset (i * 1.2)
        x = 0.4 * np.cos(frame / 10 + i * 1.2)
        y = 1.8 + 0.3 * np.sin(frame / 7 + i * 1.5)
        circle.set_center((x, y))
    return circles

# Create the animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 100, 200), interval=50, blit=True)

plt.title("Gesner Deslandes: Ice Cream App Trial", fontsize=12, color='brown')
plt.show()
