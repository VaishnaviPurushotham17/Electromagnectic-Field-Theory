import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create figure
fig = plt.figure(figsize=(10,5))

# -----------------------------
# LEFT: Surface (Sphere)
# -----------------------------
ax1 = fig.add_subplot(121, projection='3d')
ax1.set_title("Normal is Unique on Surface")

u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, np.pi, 50)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

ax1.plot_surface(x, y, z, alpha=0.2)

point_sphere, = ax1.plot([], [], [], 'ro')
normal_arrow = ax1.quiver(0,0,0,0,0,0)

ax1.set_xlim([-1.5,1.5])
ax1.set_ylim([-1.5,1.5])
ax1.set_zlim([-1.5,1.5])

# -----------------------------
# RIGHT: Curve (Circle)
# -----------------------------
ax2 = fig.add_subplot(122, projection='3d')
ax2.set_title("Tangent is Unique on Curve")

t = np.linspace(0, 2*np.pi, 200)
xc = np.cos(t)
yc = np.sin(t)
zc = np.zeros_like(t)

ax2.plot(xc, yc, zc)

point_circle, = ax2.plot([], [], [], 'ro')
tangent_arrow = ax2.quiver(0,0,0,0,0,0)

ax2.set_xlim([-1.5,1.5])
ax2.set_ylim([-1.5,1.5])
ax2.set_zlim([-1.5,1.5])

# -----------------------------
# Animation Function
# -----------------------------
def update(frame):
    global normal_arrow, tangent_arrow
    
    angle = frame * 0.05

    # ---- Sphere point ----
    theta = angle
    phi = np.pi/4
    
    px = np.cos(theta)*np.sin(phi)
    py = np.sin(theta)*np.sin(phi)
    pz = np.cos(phi)

    point_sphere.set_data([px], [py])
    point_sphere.set_3d_properties([pz])

    normal_arrow.remove()
    normal_arrow = ax1.quiver(px, py, pz, px, py, pz, length=0.5)

    # ---- Circle point ----
    cx = np.cos(angle)
    cy = np.sin(angle)
    cz = 0

    tx = -np.sin(angle)
    ty = np.cos(angle)
    tz = 0

    point_circle.set_data([cx], [cy])
    point_circle.set_3d_properties([cz])

    tangent_arrow.remove()
    tangent_arrow = ax2.quiver(cx, cy, cz, tx, ty, tz, length=0.5)

    return point_sphere, point_circle

ani = FuncAnimation(fig, update, frames=200, interval=50)

plt.show()
