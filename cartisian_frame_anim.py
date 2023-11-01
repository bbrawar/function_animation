import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function f(x) that you want to animate
def f(x):
    return np.sin(x)

# Create the x values (domain)
x = np.linspace(0, 2 * np.pi, 100)
# Create the y values (range)
y = f(x)

# Create the figure and axis
fig, ax = plt.subplots()
# Set the axis limits
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.2, 1.2)

# Create an empty plot for the initial frame
line, = ax.plot([], [])

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot for each frame
def update(frame):
    x_data = x[:frame]
    y_data = y[:frame]
    line.set_data(x_data, y_data)
    return line,

# Create the animation object
ani = FuncAnimation(fig, update, frames=len(x), init_func=init, blit=True)

# Display the animation (you can save it as well)
plt.show()
