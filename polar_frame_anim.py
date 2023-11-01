import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function r(θ) that you want to animate
def r(theta):
    return 1 + 0.5 * np.sin(5 * theta)  # Modify this function as needed

# Create an array of theta values
theta = np.linspace(0, 2 * np.pi, 1000)

# Create a figure
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.set_rmax(2)  # Set the maximum r-value for the polar plot

# Create an empty plot for the initial frame
line, = ax.plot([], [])

# Function to initialize the plot
def init():
    line.set_data([], [])
    return line,

# Function to update the plot for each frame
def update(frame):
    theta_data = theta[:frame]
    r_data = r(theta_data)
    line.set_data(theta_data, r_data)
    return line,

# Create the animation object and set a shorter interval for faster animation
# The 'interval' parameter specifies the delay between frames in milliseconds
ani = FuncAnimation(fig, update, frames=len(theta), init_func=init, blit=True, interval=20)  # Set a shorter interval (e.g., 20ms)

# Display the animation (you can save it as well)
plt.show()
