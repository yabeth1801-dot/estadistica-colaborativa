import numpy as np

datos = np.loadtxt(
    "datos.csv",
    delimiter=",",
    skiprows=1
)

ingresos = datos[:, 1]

# MEDIDAS DE TENDENCIA CENTRAL


# MEDIDAS DE DISPERSION

desviacion = np.std(ingresos)
print("Desviacion estandar del ingreso:", desviacion)