import numpy as np

np.random.seed(42)

# Generar 1000 personas
edad = np.random.randint(18, 70, 1000)

# Ingreso relacionado con la edad y con variabilidad aleatoria
ingreso = 8000 + edad * 850 + np.random.normal(0, 10000, 1000)

print("Edades:")
print(edad)

print("\nIngresos:")
print(ingreso)