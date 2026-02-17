import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fixed vector A
A = np.array([4, 0])

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.grid()

# Draw vector A (Blue)
vec_A = ax.quiver(0, 0, A[0], A[1], 
                  angles='xy', scale_units='xy', scale=1, 
                  color='blue', label='Vector A')

# Initialize other vectors
vec_B = ax.quiver(0, 0, 0, 0, 
                  angles='xy', scale_units='xy', scale=1, 
                  color='green', label='Vector B')

vec_parallel = ax.quiver(0, 0, 0, 0, 
                         angles='xy', scale_units='xy', scale=1, 
                         color='red', label='Projection (B‖)')

vec_perp = ax.quiver(0, 0, 0, 0, 
                     angles='xy', scale_units='xy', scale=1, 
                     color='purple', label='Perpendicular (B⊥)')

def update(frame):
    angle = np.deg2rad(frame)

    # Rotating B
    B = np.array([4*np.cos(angle), 4*np.sin(angle)])

    # Projection calculation
    B_parallel = (np.dot(B, A) / np.dot(A, A)) * A
    B_perp = B - B_parallel

    # Update vectors
    vec_B.set_UVC(B[0], B[1])
    vec_parallel.set_UVC(B_parallel[0], B_parallel[1])

    vec_perp.set_offsets([B_parallel[0], B_parallel[1]])
    vec_perp.set_UVC(B_perp[0], B_perp[1])

    return vec_B, vec_parallel, vec_perp

ani = FuncAnimation(fig, update, frames=360, interval=40)

plt.legend(loc='upper left')
plt.title("Vector Projection Visualization")
plt.show()
