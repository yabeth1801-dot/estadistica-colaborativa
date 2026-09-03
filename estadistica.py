import numpy as np

datos = np.loadtxt(
    "datos.csv",
    delimiter=",",
    skiprows=1
)

ingresos = datos[:, 1]

# MEDIDAS DE TENDENCIA CENTRAL


# MEDIDAS DE DISPERSION