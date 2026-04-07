# Ejemplo 1: for con range() básico
# range(inicio, fin, paso)
# Nota: el fin NO se incluye

# Contar del 1 al 5
for i in range(1, 6):
    print(f"Número: {i}")

# Del 0 al 4 (rango por defecto empieza en 0)
for i in range(5):
    print(f"Índice: {i}")

# Con paso personalizado (del 2 al 10 de 2 en 2)
for i in range(2, 11, 2):
    print(f"Pares: {i}")

# ------------------------------------------
# Ejemplo 2: for con listas y texto
# Iterar sobre texto
nombre = "Python"
for letra in nombre:
    print(f"Letra: {letra}")

# Lista de frutas
frutas = ["manzana", "pera", "uva", "naranja"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Con índice (usando enumerate)
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"Posición {indice}: {color}")

# ------------------------------------------
# Ejemplo 3: Tablas de multiplicar con for
# Tabla del 5
numero = 5
print(f"=== Tabla del {numero} ===")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Tabla personalizada
num = int(input("¿Qué tabla quieres ver? "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# ------------------------------------------
# Ejemplo 4: Sumar acumuladores con for
# Sumar los primeros 100 números
suma = 0
for i in range(1, 101):
    suma = suma + i
print(f"Suma del 1 al 100: {suma}")

# Calcular factorial
n = int(input("Factorial de: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# ------------------------------------------
# Ejemplo 5: for anidados
# Tabla de multiplicar completa (del 1 al 5)
for i in range(1, 6):
    print(f"\n=== Tabla del {i} ===")
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")

# Dibujar un rectángulo con asteriscos
filas = 4
columnas = 6
for i in range(filas):
    for j in range(columnas):
        print("*", end=" ")
    print()  # Salto de línea

# ------------------------------------------
# Mini Reto 1: Pirámide de asteriscos (for)
# Dibujar pirámide
niveles = 5
for i in range(1, niveles + 1):
    espacios = " " * (niveles - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

# ------------------------------------------
# Mini Reto 2: Fibonacci (for)
# Serie Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13...
n = int(input("¿Cuántos números de Fibonacci? "))
a, b = 0, 1

print("Serie Fibonacci:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b