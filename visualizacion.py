import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt(
    "datos.csv",
    delimiter=",",
    skiprows=1
)

edad = datos[:, 0]
ingreso = datos[:, 1]

# GRAFICA DE DISPERSION

plt.scatter(edad, ingreso)

plt.xlabel("Edad")
plt.ylabel("Ingreso")

plt.title("Relacion entre edad e ingreso")

plt.savefig("graficas/dispersion.png")

plt.close()