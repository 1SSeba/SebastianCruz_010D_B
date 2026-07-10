def validar_codigo(codigo): return len(codigo.strip()) > 0
def validar_titulo(titulo): return len(titulo.strip()) > 0
def validar_genero(genero): return len(genero.strip()) > 0
def validar_idioma(idioma): return len(idioma.strip()) > 0
def validar_duracion(duracion): return duracion > 0
def validar_precio(precio): return precio > 0
def validar_cupos(cupos): return cupos > 0
def validar_clasificacion(clasificacion): return clasificacion == "A" or clasificacion == "B" or clasificacion == "C"
def validar_3d(es_3d): return

def cupos_genero(cupo, genero, peliculas, cartelera):
    cupo = 0
    for cod, datos in peliculas.items():
        if datos[1].lower ==  genero.lower:
            cupo += cartelera[cod][1]
    return cupo

def busqueda_precio(p_min, p_max, peliculas, cartelera):
    precio = []
    for cod, datos in cartelera.items():
        if p_min <= datos[0] <= p_max and datos[1] > 0:
            precio.append(f"{peliculas[cod][0]}, {cartelera[cod][0]}")
        precio.sort()
    return precio

def buscar_codigo(codigo, peliculas):
    return codigo in peliculas

def actualizar_precio(precio, peliculas, cartelera):
    codigo = input("Ingrese el código de la película a actualizar: ")
    if buscar_codigo(codigo):
        cartelera[codigo][0] = precio
        print(f"El precio de la película '{peliculas[codigo][0]}' ha sido actualizado a {precio}.")
    else:
        print("Código de película no encontrado.")

def desplegar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por género")
    print("2. Búsqueda de películas por rango de precio")
    print("3. Actualizar precio de película")
    print("4. Agregar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("=====================================")

def agregar_pelicula(codigo, titulo, genero, duracion, idioma, es_3d, precio, cupos, clasificacion, peliculas, cartelera):
    if not validar_codigo(codigo):
        print("Código inválido. Debe tener al menos un carácter.")
        return
    if not validar_titulo(titulo):
        print("Título inválido. Debe tener al menos un carácter.")
        return
    if not validar_genero(genero):
        print("Género inválido. Debe tener al menos un carácter.")
        return
    if not validar_duracion(duracion):
        print("Duración inválida. Debe ser mayor a 0.")
        return
    if not validar_idioma(idioma):
        print("Idioma inválido. Debe tener al menos un carácter.")
        return
    if not validar_3d(es_3d):
        print("Valor de 3D inválido. Debe ser True o False.")
        return
    if not validar_precio(precio):
        print("Precio inválido. Debe ser mayor a 0.")
        return
    if not validar_cupos(cupos):
        print("Cupos inválidos. Deben ser mayores a 0.")
        return
    if not validar_clasificacion(clasificacion):
        print("Clasificación inválida. Debe ser 'A', 'B' o 'C'.")
        return

    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    print(f"Película '{titulo}' agregada exitosamente.")

def eliminar_pelicula(peliculas, cartelera):
    codigo = input("Ingrese el código de la película a eliminar: ")
    if buscar_codigo(codigo, peliculas):
        del peliculas[codigo]
        del cartelera[codigo]
        print(f"La película con código '{codigo}' ha sido eliminada.")
    else:
        print("Código de película no encontrado.")

def leer_op():
    try:
        opcion = int(input("Ingrese un número: "))
        if opcion < 1 or opcion > 6:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 6.")
            return leer_op()
        return opcion
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        return leer_op()

def main():
    peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    }

    cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    }

    while True:
        desplegar_menu()
        opcion = int(input("Ingrese un numero: "))
        leer_op(opcion)
        if opcion == 1:
            genero = input("Ingrese el género de la película: ")
            cupos = cupos_genero(0, genero, peliculas, cartelera)
            print(f"El cupo total de películas del género '{genero}' es: {cupos}")

        elif opcion == 2:
            p_min = float(input("Ingrese el precio mínimo: "))
            p_max = float(input("Ingrese el precio máximo: "))
            resultados = busqueda_precio(p_min, p_max, peliculas, cartelera)
            print("Películas encontradas:")
            for pelicula in resultados:
                print(pelicula)
        elif opcion == 3:
            precio = float(input("Ingrese el nuevo precio: "))
            actualizar_precio(precio, peliculas, cartelera)
        elif opcion == 4:
            codigo = input("Ingrese el código de la película: ")
            titulo = input("Ingrese el título de la película: ")
            genero = input("Ingrese el género de la película: ")
            duracion = int(input("Ingrese la duración de la película (en minutos): "))
            idioma = input("Ingrese el idioma de la película: ")
            es_3d = input("¿La película es 3D? (True/False): ").strip().lower() == 'true'
            precio = float(input("Ingrese el precio de la película: "))
            cupos = int(input("Ingrese los cupos disponibles para la película: "))
            clasificacion = input("Ingrese la clasificación de la película (A, B, C): ").strip().upper()
            agregar_pelicula(codigo, titulo, genero, duracion, idioma, es_3d, precio, cupos, clasificacion, peliculas, cartelera)
        elif opcion == 5:
            eliminar_pelicula(peliculas, cartelera)
        elif opcion == 6:
            break

main()