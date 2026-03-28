import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Fixed vector B
B = np.array([0, 1, 0])  # along y-axis

def update(frame):
    ax.clear()
    
    # Rotating vector A in XY plane
    angle = frame * 0.1
    A = np.array([np.cos(angle), np.sin(angle), 0])
    
    # Cross product
    C = np.cross(A, B)
    
    # Plot A (Red)
    ax.quiver(0,0,0, A[0], A[1], A[2], color='red')
    
    # Plot B (Black)
    ax.quiver(0,0,0, B[0], B[1], B[2], color='black')
    
    # Plot Cross Product (Blue)
    ax.quiver(0,0,0, C[0], C[1], C[2], color='blue')
    
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])
    
    ax.set_title("Cross Product: A × B (Perpendicular Vector)")

ani = FuncAnimation(fig, update, frames=100, interval=100)
plt.show()