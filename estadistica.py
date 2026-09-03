import numpy as np

datos = np.loadtxt(
    "datos.csv",
    delimiter=",",
    skiprows=1
)

ingresos = datos[:, 1]

# MEDIDAS DE TENDENCIA CENTRAL

media = np.mean(ingresos)
print("Media del ingreso:", media)

# MEDIDAS DE DISPERSION