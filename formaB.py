def validar_codigo(codigo): return len(codigo.strip()) > 0
def validar_nombre(nombre): return len(nombre.strip()) > 0
def validar_tickets(cantidad): return cantidad > 0

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

def leer_op():
    if leer_op < 0:
        return print("La opcion debe de ser mayor a 0")

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
        opcion = int(input(leer_op()))
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
        elif opcion == 5:
        elif opcion == 6:
            break