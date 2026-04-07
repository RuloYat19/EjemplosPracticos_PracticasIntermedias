# Ejemplo 1: Función sin parámetros ni return
# Función simple que solo imprime
def saludar():
    print("¡Hola! Bienvenido al taller")
    print("Hoy aprenderemos funciones")

# Llamar a la función
saludar()
saludar()  # Se puede llamar varias veces

# Función con mensaje personalizado
def mostrar_menu():
    print("=" * 30)
    print("    MENÚ PRINCIPAL")
    print("=" * 30)
    print("1. Iniciar")
    print("2. Configuración")
    print("3. Salir")
    print("=" * 30)

mostrar_menu()

# ------------------------------------------
# Ejemplo 2: Función con parámetros (sin return)
# Función con un parámetro
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("Ana")
saludar_persona("Luis")
saludar_persona("Carlos")

# Función con múltiples parámetros
def presentar(nombre, edad, ciudad):
    print(f"Me llamo {nombre}")
    print(f"Tengo {edad} años")
    print(f"Soy de {ciudad}")

presentar("María", 25, "Guatemala")

# Función con parámetros por defecto
def saludar_con_estilo(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!")

saludar_con_estilo("Ana")           # Usa "Hola" por defecto
saludar_con_estilo("Luis", "Buenas") # Usa "Buenas"

# ------------------------------------------
# Ejemplo 3: Función con return (devuelve valor)
# Función que suma y devuelve resultado
def sumar(a, b):
    resultado = a + b
    return resultado

# Usar el valor retornado
mi_suma = sumar(5, 3)
print(f"La suma es: {mi_suma}")

# Usar directamente
print(f"Suma: {sumar(10, 20)}")

# Múltiples operaciones
def calcular_area_circulo(radio):
    area = 3.14159 * (radio ** 2)
    return area

area1 = calcular_area_circulo(5)
area2 = calcular_area_circulo(10)
print(f"Área radio 5: {area1:.2f}")
print(f"Área radio 10: {area2:.2f}")

# ------------------------------------------
# Ejemplo 4: Funciones con múltiples return
def clasificar_numero(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

print(clasificar_numero(10))   # positivo
print(clasificar_numero(-5))   # negativo
print(clasificar_numero(0))    # cero

# Función que devuelve varios valores (tupla)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

# Recibir múltiples valores
s, r, m, d = operaciones_basicas(10, 3)
print(f"Suma: {s}, Resta: {r}, Multi: {m}, Div: {d:.2f}")

# ------------------------------------------
# Ejemplo 5: Funciones que llaman a otras funciones
def es_par(numero):
    return numero % 2 == 0

def es_impar(numero):
    return not es_par(numero)  # Llama a es_par()

def analizar_numero(numero):
    if es_par(numero):
        return f"{numero} es par"
    else:
        return f"{numero} es impar"

print(analizar_numero(7))  # 7 es impar
print(analizar_numero(8))  # 8 es par

# Ejemplo más complejo
def obtener_descuento(total):
    if total > 1000:
        return 0.20  # 20% descuento
    elif total > 500:
        return 0.10  # 10% descuento
    else:
        return 0

def calcular_total_con_descuento(total):
    descuento = obtener_descuento(total)
    ahorro = total * descuento
    total_final = total - ahorro
    return total_final, ahorro

total_final, ahorrado = calcular_total_con_descuento(1500)
print(f"Total: $1500, Ahorro: ${ahorrado}, Pagas: ${total_final}")

# ------------------------------------------
# Mini Reto 1: Generador de contraseñas
import random
import string

def generar_password(longitud=8):
    caracteres = string.ascii_letters + string.digits + "!@#$%"
    password = ""
    for i in range(longitud):
        password += random.choice(caracteres)
    return password

# Probar
print(generar_password())      # 8 caracteres
print(generar_password(12))    # 12 caracteres
print(generar_password(16))    # 16 caracteres