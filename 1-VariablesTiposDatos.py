# Ejemplo 1: Crear variables de diferentes tipos
# Entero (int)
edad = 25
año_actual = 2024

# Decimal (float)
precio = 19.99
pi = 3.1416

# Texto (str)
nombre = "Ana"
ciudad = 'Guatemala'

# Booleano (bool)
es_estudiante = True
tiene_mascota = False

# Ver los tipos
print(type(edad))        # <class 'int'>
print(type(precio))      # <class 'float'>
print(type(nombre))      # <class 'str'>
print(type(es_estudiante)) # <class 'bool'>

# ------------------------------------------
# Ejemplo 2: Cambiar el valor de una variable
# Las variables pueden cambiar de valor
puntaje = 10
print(puntaje)  # 10

puntaje = 25
print(puntaje)  # 25

# Incluso pueden cambiar de tipo (aunque no es recomendado)
dato = 100
dato = "ahora soy texto"
print(dato)

# ------------------------------------------
# Ejemplo 3: Nombres descriptivos (buena práctica)
# ❌ Malos nombres
a = 5
b = "Juan"
x = True

# ✅ Buenos nombres
cantidad_hijos = 2
nombre_cliente = "María"
es_mayor_de_edad = True

# ------------------------------------------
# Ejemplo 4: Operaciones con diferentes tipos
# Enteros
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3 (división entera)
print(a % b)   # 1 (residuo)
print(a ** b)  # 1000 (10^3)

# Texto
nombre = "Carlos"
apellido = "García"
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # Carlos García

# Repetición de texto
print("-" * 20)  # imprime 20 guiones

# ------------------------------------------
# Ejemplo 5: Input del usuario (conversión de tipos)
# Texto directo
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)

# Convertir a número (importante)
edad = int(input("¿Cuántos años tienes? "))
print("El año que viene tendrás", edad + 1)

# Número decimal
altura = float(input("¿Cuánto mides? (en metros): "))
print("Tu altura es", altura, "metros")