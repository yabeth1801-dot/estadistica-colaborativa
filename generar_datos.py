import numpy as np

np.random.seed(42)

# =====================================
# DATOS NUMERICOS
# =====================================

edad = np.random.randint(18, 70, 1000)

ingreso = 8000 + edad * 850 + np.random.normal(0, 10000, 1000)

datos = np.column_stack((edad, ingreso))

np.savetxt(
    "datos.csv",
    datos,
    delimiter=",",
    header="edad,ingreso",
    comments=""
)

# =====================================
# DATOS CATEGORICOS
# =====================================

categorias = np.array([
    ["Tecnologia", 350],
    ["Salud", 280],
    ["Educacion", 220],
    ["Otros", 150]
])

np.savetxt(
    "categorias.csv",
    categorias,
    delimiter=",",
    fmt="%s",
    header="categoria,cantidad",
    comments=""
)

print("Datos guardados correctamente.")