import numpy as np
y_0 = 0 
x_0 = 0
v_0 = 15
alpha = np.pi / 180 * 45
vx_0 =v * np.cos(alpha)
vy_0  = v * np.sin(alpha)

coords = []
for in nparange (0, 5, 0.01)
x = x_0 + vx_0 * t 
y = y_0 * t - g  * t**2 / 2
coords.append([t, x, y])
