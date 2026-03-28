import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6,6))

# Fixed vector B
B = np.array([2, 0])  # along x-axis

def update(frame):
    ax.clear()
    
    # Rotating vector A (applied field)
    angle = frame * 0.1
    A = np.array([2*np.cos(angle), 2*np.sin(angle)])
    
    # Unit vector of B
    B_unit = B / np.linalg.norm(B)
    
    # Projection of A onto B
    proj_length = np.dot(A, B_unit)
    proj_vector = proj_length * B_unit
    
    # Plot vectors
    ax.quiver(0, 0, A[0], A[1], angles='xy', scale_units='xy', scale=1, color='red', label='A (Applied)')
    ax.quiver(0, 0, B[0], B[1], angles='xy', scale_units='xy', scale=1, color='black', label='B (Reference)')
    ax.quiver(0, 0, proj_vector[0], proj_vector[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Projection')
    
    # Draw dashed line (projection drop)
    ax.plot([A[0], proj_vector[0]], [A[1], proj_vector[1]], 'k--')
    
    # Dot product value
    dot = np.dot(A, B)
    ax.text(-2.5, 2.5, f"A · B = {dot:.2f}", fontsize=12)
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_title("Dot Product = Projection of A onto B")
    ax.grid()

ani = FuncAnimation(fig, update, frames=100, interval=100)
plt.show()