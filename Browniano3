import numpy as np
import matplotlib.pyplot as plt

m = 1.0          # Masa
q = 1.0          # Carga
B_mag = 5.0      # Intensidad del campo magnético (en z)
beta = 0.5       # Coeficiente de fricción
kB = 1.38e-23    # Constante de Boltzmann (usaremos un valor arbitrario 1.0 para fines visuales)
T = 1.0          # Temperatura
dt = 0.01        # Paso de tiempo
steps = 5000     # Número de pasos

# Factor de la intensidad del ruido
noise_scale = np.sqrt(2 * beta * 1.0 * T) # Usando kB=1 para visualización

v = np.array([1.0, 0.0, 0.0]) # Velocidad inicial (Vx, Vy, Vz)
r = np.array([0.0, 0.0, 0.0]) # Posición inicial (x, y, z)

posiciones = np.zeros((steps, 3))

for i in range(steps):
    # 1. Fuerza de Lorentz (producto cruz -qB x V)
    # Para B = (0, 0, B_mag), -q(B x V) es (-q*B*Vy, q*B*Vx, 0)
    f_lorentz = np.array([-q * B_mag * v[1], q * B_mag * v[0], 0])
    
    # 2. Ruido Gaussiano (Gamma * sqrt(dt))
    # El ruido se escala por sqrt(dt) para mantener la varianza correcta
    ruido = np.random.normal(0, 1, 3) * noise_scale * np.sqrt(dt)
    
    # 3. Actualizar Velocidad: dV = (1/m) * (-beta*V + F_lorentz) * dt + (1/m) * Ruido
    dv = ((-beta * v + f_lorentz) / m) * dt + (ruido / m)
    v += dv
    
    # 4. Actualizar Posición
    r += v * dt
    posiciones[i] = r

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(posiciones[:, 0], posiciones[:, 1], posiciones[:, 2], lw=0.5)
ax.set_title("Movimiento Browniano en un Campo Magnético (B en eje Z)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
