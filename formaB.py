def validar_codigo(codigo): return len(codigo.strip()) > 0
def validar_nombre(nombre): return len(nombre.strip()) > 0
def validar_tickets(cantidad): return cantidad > 0
def validar_promedio(promedio): return 1.0 <= promedio <= 7.0



def cupos_genero(cupo, genero, peliculas, categoraias):
    cupo = 0
    for cod, datos in peliculas.items():
        if datos[1].lower ==  genero.lower:
            cupo += cartelera[cod][1]
    return cupo

def busqueda_rango(pmin, pmax, peliculas, cartelera):
    precio = []
    for cod, datos in cartelera.items():
        if pmin <= datos[0] <= pmax and datos[1] > 0:
            precio.append(f"{peliculas[cod][0]}, {cartelera[0]}")
        precio.sort()
    return precio

def menu():
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
        opcion = int(input(leer_op()))
        if opcion = 1:
        elif opcion = 2:
        elif opcion = 3:
        elif opcion = 4:
        elif opcion = 5:
        elif opcion = 6:
            break