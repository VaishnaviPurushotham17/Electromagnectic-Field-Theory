import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# -------- Permittivity Tensor --------
epsilon = np.array([[4, 0, 0],
                    [0, 8, 0],
                    [0, 0, 5]])
# change the matrix values to see different anisotropic behaviors. For example, you can set epsilon[0, 0] = 2 to make the x-axis less responsive to the electric field, or increase epsilon[1, 1] to make the y-axis more responsive. The off-diagonal elements can also be modified to introduce coupling between different axes, which would result in more complex field interactions.
# -------- Create Figure --------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# -------- Update Function --------
def update(frame):
    ax.cla()

    # Axis limits
    ax.set_xlim([-6, 6])
    ax.set_ylim([-6, 6])
    ax.set_zlim([-6, 6])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("Applied Field (Blue) vs Resultant Field (Red)")

    # Rotating E vector
    theta = np.radians(frame)
    phi = np.radians(frame / 2)

    Ex = np.cos(theta)
    Ey = np.sin(theta)
    Ez = np.sin(phi)

    E = np.array([Ex, Ey, Ez])

    # Compute D
    D = epsilon @ E

    # ---- Plot Applied Electric Field (Blue) ----
    ax.quiver(0, 0, 0,
              E[0]*3, E[1]*3, E[2]*3,
              color='blue',
              linewidth=2,
              label='Applied Field (E)')

    # ---- Plot Resultant Displacement Field (Red) ----
    ax.quiver(0, 0, 0,
              D[0]/3, D[1]/3, D[2]/3,
              color='red',
              linewidth=2,
              label='Resultant Field (D)')

    ax.legend()

# -------- Animation --------
ani = FuncAnimation(fig, update, frames=360, interval=40)

plt.show()
