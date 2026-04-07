# Ejemplo 1: Los 7 operadores básicos
a = 15
b = 4

print("a =", a, "b =", b)
print("-" * 30)

print("Suma (a + b):", a + b)           # 19
print("Resta (a - b):", a - b)           # 11
print("Multiplicación (a * b):", a * b)   # 60
print("División (a / b):", a / b)         # 3.75
print("División entera (a // b):", a // b) # 3 (solo la parte entera)
print("Módulo o residuo (a % b):", a % b)  # 3 (lo que sobra)
print("Potencia (a ** b):", a ** b)       # 15^4 = 50625

# ------------------------------------------
# Ejemplo 2: Prioridad de operadores (igual que matemáticas)
# Primero multiplicación/división, luego suma/resta
resultado1 = 5 + 3 * 2
print("5 + 3 * 2 =", resultado1)  # 11, no 16

# Usar paréntesis para cambiar el orden
resultado2 = (5 + 3) * 2
print("(5 + 3) * 2 =", resultado2)  # 16

# Ejemplo más complejo
resultado3 = (10 + 2) * 3 - 8 / 2
print("(10 + 2) * 3 - 8 / 2 =", resultado3)  # 36 - 4 = 32

# ------------------------------------------
# Ejemplo 3: Módulo (%) - muy útil en programación
# Saber si un número es par o impar
numero = 17
if numero % 2 == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")

# Saber si un número es múltiplo de otro
print("¿10 es múltiplo de 3?", 10 % 3 == 0)  # False
print("¿15 es múltiplo de 5?", 15 % 5 == 0)  # True

# Útil para ciclos (cada 3 elementos)
for i in range(1, 11):
    if i % 3 == 0:
        print(i, "es múltiplo de 3")

# ------------------------------------------
# Ejemplo 4: División entera (//) y residuo (%) juntos
# Convertir segundos a minutos y segundos
segundos_totales = 185
minutos = segundos_totales // 60
segundos = segundos_totales % 60

print(f"{segundos_totales} segundos = {minutos} minutos y {segundos} segundos")
# 185 segundos = 3 minutos y 5 segundos

# Convertir minutos a horas
minutos_totales = 135
horas = minutos_totales // 60
minutos_restantes = minutos_totales % 60

print(f"{minutos_totales} minutos = {horas} horas y {minutos_restantes} minutos")

# ------------------------------------------
# Ejemplo 5: Operadores de asignación combinados 
contador = 10
print("Inicio:", contador)

contador += 5   # contador = contador + 5
print("+= 5:", contador)  # 15

contador -= 3   # contador = contador - 3
print("-= 3:", contador)  # 12

contador *= 2   # contador = contador * 2
print("*= 2:", contador)  # 24

contador //= 4  # contador = contador // 4
print("//= 4:", contador)  # 6

contador %= 4   # contador = contador % 4
print("%= 4:", contador)  # 2