import numpy as np
import matplotlib.pyplot as plt
MODE = "STABLE"
G = 6.674e-11
dt = 3600

bodies = [[1,2,3,4,5]]

if MODE == "STABLE":
    # Sun - Earth - Moon
    m1, x1, y1, vx1, vy1 = 1.989e30, 0, 0, 0, 0
    m2, x2, y2, vx2, vy2 = 5.972e24, 1.496e11, 0, 0, 29780
    m3, x3, y3, vx3, vy3 = 7.348e22, 1.496e11 + 384400000, 0, 0, 29780 + 1022
    steps, title = 24*365, " Stable (Procedure)"
else:
    # 3 Stars (High speed to fly off)
    m = 1.989e30
    m1, x1, y1, vx1, vy1 = m, 1e11,0,0,30000
    m2, x2, y2, vx2, vy2 = m, -1e11,0,0,-30000
    m3, x3, y3, vx3, vy3 = m, 0,1e11,-30000,0
    steps, title = 24*365, " Chaotic (Procedure)"
    
hist1_x, hist1_y = [], []
hist2_x, hist2_y = [], []
hist3_x, hist3_y = [], []

for step in range(steps):
    # Calculate distances
    r12 = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    r13 = np.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    r23 = np.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    
    # Calculate forces
    F12 = G * m1 * m2 / r12**2
    F13 = G * m1 * m3 / r13**2
    F23 = G * m2 * m3 / r23**2
    
    # Update velocities and positions using Euler's method
    vx1 += (F12 * (x2 - x1) / r12 + F13 * (x3 - x1) / r13) * dt / m1 # F/m = a, a*dt = dv, x component of unit vector * (x2-x1) / r12   
    vy1 += (F12 * (y2 - y1) / r12 + F13 * (y3 - y1) / r13) * dt / m1
    vx2 += (-F12 * (x2 - x1) / r12 + F23 * (x3 - x2) / r23) * dt / m2
    vy2 += (-F12 * (y2 - y1) / r12 + F23 * (y3 - y2) / r23) * dt / m2
    vx3 += (-F13 * (x3 - x1) / r13 - F23 * (x3 - x2) / r23) * dt / m3
    vy3 += (-F13 * (y3 - y1) / r13 - F23 * (y3 - y2) / r23) * dt / m3
    
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

# Plot the trajectories
linewidth = 3
plt.figure(figsize=(10, 8))
plt.plot(hist1_x, hist1_y, 'y-', label='Star 1', linewidth=linewidth)
plt.plot(hist2_x, hist2_y, 'b-', label='Star 2', linewidth=linewidth)
plt.plot(hist3_x, hist3_y, 'g-', label='Star 3', linewidth=linewidth)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title(title)
plt.legend()
plt.grid(True)
plt.savefig(f'{MODE.lower()}_three_body.png')
plt.show()

e_m_relative_x = np.asarray(hist2_x) - np.asarray(hist3_x)
e_m_relative_y = np.asarray(hist2_y) - np.asarray(hist3_y)
plt.figure(figsize=(10, 8))
plt.plot(e_m_relative_x, e_m_relative_y, 'm-', label='Earth-Moon Relative', linewidth=linewidth)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Earth-Moon Relative Trajectory')
plt.legend()
plt.grid(True)
plt.savefig(f'earth_moon_relative_{MODE.lower()}.png')