# EJEMPLOS CON FOR
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
# EJEMPLOS CON WHILE
# Ejemplo 1: while básico (contador)
# Contar del 1 al 5
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # IMPORTANTE: evitar bucle infinito

# Contador descendente
numero = 10
while numero > 0:
    print(numero)
    numero -= 1
print("¡Despegue!")

# ------------------------------------------
# Ejemplo 2: Validación de entrada (muy útil)
# Pedir un número positivo
numero = -1
while numero < 0:
    numero = int(input("Ingresa un número positivo: "))
    if numero < 0:
        print("Error: debe ser positivo")
print(f"¡Correcto! Número: {numero}")

# ------------------------------------------
# Ejemplo 3: Menú interactivo (while True + break)
# Validar rango (1-10)
valor = 0
while valor < 1 or valor > 10:
    valor = int(input("Ingresa un número entre 1 y 10: "))
print(f"Número válido: {valor}")

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("¡Hola! ¿Cómo estás?")
    elif opcion == "2":
        print("¡Hasta luego!")
    elif opcion == "3":
        print("Saliendo del programa...")
        break  # Sale del bucle
    else:
        print("Opción inválida")

# ------------------------------------------
# Ejemplo 4: Juego de adivinanza (while)
import random

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("Adivina el número (1-100)")

while not adivinado:
    numero = int(input("Tu intento: "))
    intentos += 1
    
    if numero == secreto:
        print(f"🎉 Correcto en {intentos} intentos")
        adivinado = True
    elif numero < secreto:
        print("📈 Más alto")
    else:
        print("📉 Más bajo")

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