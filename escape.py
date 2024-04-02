import math

G = 6.67430e-11  # Constante de gravitacional de la tierra
M = 5.972e24    # Masa de la Tierra en kg
R = 6371000     # Radio de la Tierra en metros

def calcular_velocidad_escape(masa_planeta, radio_planeta):
    return (2 * G * masa_planeta / radio_planeta) ** 0.5

velocidad_escape = calcular_velocidad_escape(M, R)

print(f"La velocidad de escape de la Tierra es {velocidad_escape} m/s.")