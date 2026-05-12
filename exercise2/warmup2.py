import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
def calc_force(m1, m2, x1, y1, x2, y2, G):
    r = ((x2-x1)**2 + (y2-y1)**2)**0.5
    F = G * m1 * m2 / r**2
    theta = np.arctan2(y2-y1, x2-x1)
    Fx = F * np.cos(theta)
    Fy = F * np.sin(theta)
    return Fx, Fy # from 2 on 1, so we need to add to 1 and subtract from 2


def calc_trajectories(MODE="STABLE", nsteps=24*365, dt=3600, G = 6.674e-11):
    if MODE == "STABLE":
        # Sun - Earth - Moon
        m1, x1, y1, vx1, vy1 = 1.989e30, 0, 0, 0, 0
        m2, x2, y2, vx2, vy2 = 5.972e24, 1.496e11, 0, 0, 29780
        m3, x3, y3, vx3, vy3 = 7.348e22, 1.496e11 + 384400000, 0, 0, 29780 + 1022
        title = " Stable (Procedure)"
    else:
        # 3 Stars (High speed to fly off)
        m = 1.989e30
        m1, x1, y1, vx1, vy1 = m, 1e11,0,0,30000
        m2, x2, y2, vx2, vy2 = m, -1e11,0,0,-30000
        m3, x3, y3, vx3, vy3 = m, 0,1e11,-30000,0
        title = " Chaotic (Procedure)"
        
    hist1_x, hist1_y = [], []
    hist2_x, hist2_y = [], []
    hist3_x, hist3_y = [], []

    for step in range(nsteps):
        f_12_x, f_12_y = calc_force(m1, m2, x1, y1, x2, y2, G)
        f_13_x, f_13_y = calc_force(m1, m3, x1, y1, x3, y3, G)
        f_23_x, f_23_y = calc_force(m2, m3, x2, y2, x3, y3, G)
        # Update velocities and positions using Euler's method
        vx1 += (f_12_x + f_13_x) * dt / m1 # F/m = a, a*dt = dv, x component of unit vector * (x2-x1) / r12   
        vy1 += (f_12_y + f_13_y) * dt / m1
        vx2 += (-f_12_x + f_23_x) * dt / m2
        vy2 += (-f_12_y + f_23_y) * dt / m2
        vx3 += (-f_13_x - f_23_x) * dt / m3
        vy3 += (-f_13_y - f_23_y) * dt / m3
        
        x1 += vx1 * dt
        y1 += vy1 * dt
        x2 += vx2 * dt
        y2 += vy2 * dt
        x3 += vx3 * dt
        y3 += vy3 * dt
        
        hist1_x.append(x1)
        hist1_y.append(y1)
        hist2_x.append(x2)
        hist2_y.append(y2)
        hist3_x.append(x3)
        hist3_y.append(y3)
    return hist1_x, hist1_y, hist2_x, hist2_y, hist3_x, hist3_y, title

hist1_x, hist1_y, hist2_x, hist2_y, hist3_x, hist3_y, title = calc_trajectories(MODE="CHAOTIC")

fig, ax = plt.subplots()
line1, = ax.plot([], [], 'o-', label='Body 1', linewidth=3)
line2, = ax.plot([], [], 'o-', label='Body 2', linewidth=3)
line3, = ax.plot([], [], 'o-', label='Body 3', linewidth=3)
ax.set_title(title)
ax.legend()

def update(frame):
    line1.set_data(hist1_x[:frame], hist1_y[:frame])
    line2.set_data(hist2_x[:frame], hist2_y[:frame])
    line3.set_data(hist3_x[:frame], hist3_y[:frame])
    #ax.set_xlim(min(hist1_x), max(hist1_x))
    #ax.set_ylim(min(hist1_y), max(hist1_y))
    ax.set_xlim(-2e11, 2e11)
    ax.set_ylim(-2e11, 2e11)

    return line1, line2, line3

ani = FuncAnimation(fig, update, frames=range(0, len(hist1_x), 10), blit=False)
plt.show()

