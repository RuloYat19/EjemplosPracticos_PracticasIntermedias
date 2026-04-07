# Ejemplo 1: Estructura básica (if/else)
# Evaluar si eres mayor de edad
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad")
    print("Puedes votar y sacar tu cédula")
else:
    print("Eres menor de edad")
    print("Aún necesitas permiso de tus padres")

# ------------------------------------------
# Ejemplo 2: Múltiples condiciones (if/elif/else)
# Clasificar edades
edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida")
elif edad <= 12:
    print("Eres un niño/a")
elif edad <= 18:
    print("Eres adolescente")
elif edad <= 60:
    print("Eres adulto/a")
else:
    print("Eres adulto mayor")

# ------------------------------------------
# Ejemplo 3: Operadores de comparación en acción
nota = float(input("Ingresa tu nota (0-100): "))

if nota >= 90:
    print("Excelente! 🎉")
elif nota >= 70:
    print("Aprobado 👍")
elif nota >= 60:
    print("Por poco 😅")
elif nota >= 0:
    print("Reprobado 😢")
else:
    print("Nota inválida")

# ------------------------------------------
# Ejemplo 4: Operadores lógicos (and, or, not)
# AND - ambas condiciones deben cumplirse
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# OR - al menos una condición debe cumplirse
dia = "sábado"
es_fin_de_semana = (dia == "sábado" or dia == "domingo")

if es_fin_de_semana:
    print("¡A descansar!")
else:
    print("A trabajar")

# NOT - invierte la condición
usuario_activo = False

if not usuario_activo:
    print("Por favor, activa tu cuenta")

# ------------------------------------------
# Ejemplo 5: Anidar condicionales (if dentro de if)
# Sistema de acceso a un edificio
rol = input("¿Eres 'estudiante', 'profesor' o 'admin'? ")
horario = int(input("¿Qué hora es? (0-23): "))

if rol == "admin":
    print("Acceso total permitido")
elif rol == "profesor":
    if 6 <= horario <= 20:
        print("Acceso permitido - Horario laboral")
    else:
        print("Acceso denegado - Fuera de horario")
elif rol == "estudiante":
    if 7 <= horario <= 18:
        print("Acceso permitido - Clases en curso")
    else:
        print("Acceso denegado - Biblioteca cerrada")
else:
    print("Rol no reconocido")

# ------------------------------------------
# Mini Reto: El juego del número secreto
# Adivina el número
numero_secreto = 7

print("=== ADIVINA EL NÚMERO (1-10) ===")
intento = int(input("Tu intento: "))

if intento == numero_secreto:
    print("🎉 ¡Felicidades! Adivinaste")
elif intento < numero_secreto:
    print("📈 Muy bajo... intenta más alto")
elif intento > numero_secreto:
    print("📉 Muy alto... intenta más bajo")

# BONUS: con validación de rango
if intento < 1 or intento > 10:
    print("⚠️ Recuerda que es entre 1 y 10")