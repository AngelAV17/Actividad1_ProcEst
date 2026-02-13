import numpy as np
import matplotlib.pyplot as plt

def gillespie_toggle_switch(alpha, beta, Kr, n, Omega, T_max):
    # Estado inicial: r1 y r2 en número de moléculas (enteros)
    r1, r2 = 10, 5 
    t = 0
    
    # Listas para almacenar la trayectoria
    time_history = [t]
    r1_history = [r1]
    r2_history = [r2]
    
    while t < T_max:
        c1 = r1 / Omega
        c2 = r2 / Omega
        
        # Producción de r1 (inhibida por c2)
        v1 = alpha * Omega / (1 + (c2 / Kr)**n)
        # Producción de r2 (inhibida por c1)
        v2 = alpha * Omega / (1 + (c1 / Kr)**n)
        # Degradación de r1
        v3 = beta * r1
        # Degradación de r2
        v4 = beta * r2
        
        a0 = v1 + v2 + v3 + v4
        
        if a0 == 0: break 
            

        r1_rand = np.random.random()
        dt = -np.log(r1_rand) / a0
        

        r2_rand = np.random.random() * a0
        
        if r2_rand < v1:
            r1 += 1
        elif r2_rand < v1 + v2:
            r2 += 1
        elif r2_rand < v1 + v2 + v3:
            r1 -= 1
        else:
            r2 -= 1
            
        t += dt
        
   
        time_history.append(t)
        r1_history.append(r1)
        r2_history.append(r2)
        
    return np.array(time_history), np.array(r1_history), np.array(r2_history)

# Parámetros del problema
params = {'alpha': 2, 'beta': 1, 'Kr': 1, 'n': 2, 'T_max': 500}

# Simulación con Omega pequeño (Spontaneous switching)
t_low, r1_low, r2_low = gillespie_toggle_switch(**params, Omega=10)

# Simulación con Omega grande (Estabilidad determinista)
t_high, r1_high, r2_high = gillespie_toggle_switch(**params, Omega=100)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t_low, r1_low/10, label='r1 (Normalizado)')
plt.plot(t_low, r2_low/10, label='r2 (Normalizado)')
plt.title("Omega = 10 (Alta probabilidad de cambio)")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t_high, r1_high/100, label='r1 (Normalizado)')
plt.plot(t_high, r2_high/100, label='r2 (Normalizado)')
plt.title("Omega = 100 (Estabilidad robusta)")
plt.legend()

plt.show()
