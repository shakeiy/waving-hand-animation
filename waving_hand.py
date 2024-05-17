import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure, axis, and plot elements
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Create the hand (a simple circle) and the arm (a line)
hand, = ax.plot([], [], 'o-', lw=2)
arm, = ax.plot([], [], lw=2)

# Initialization function to set up the background of each frame
def init():
    hand.set_data([], [])
    arm.set_data([], [])
    return hand, arm

# Animation function called sequentially to update the hand and arm positions
def animate(i):
    # Arm angle in radians (waving motion)
    angle = 0.2 * np.sin(i * 0.1)
    
    # Arm length
    arm_length = 1
    
    # Calculate hand position
    x_hand = arm_length * np.sin(angle)
    y_hand = arm_length * np.cos(angle)
    
    # Update hand and arm positions
    hand.set_data([x_hand], [y_hand])
    arm.set_data([0, x_hand], [0, y_hand])
    
    return hand, arm

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

# Display the animation
plt.show()
