import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6,6))

def update(frame):
    ax.clear()
    
    # Time varying applied field
    angle = frame * 0.1
    
    # Resultant vector (applied field)
    Ex = 3 * np.cos(angle)
    Ey = 3 * np.sin(angle)
    
    # Magnitude
    mag = np.sqrt(Ex**2 + Ey**2)
    
    # Unit vector (direction only)
    ux = Ex / mag
    uy = Ey / mag
    
    # Plot resultant vector (RED)
    ax.quiver(0, 0, Ex, Ey, color='red', scale=10)
    
    # Plot unit vector (BLUE)
    ax.quiver(0, 0, ux, uy, color='blue', scale=5)
    
    # Labels
    ax.text(Ex, Ey, 'Resultant Field', color='red')
    ax.text(ux, uy, 'Unit Vector', color='blue')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.set_title("Applied Field → Resultant Vector → Unit Vector")
    ax.grid()

ani = FuncAnimation(fig, update, frames=100, interval=100)
plt.show()