def validar
def validar
def validar
def validar

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
        print("La opcion debe de ser mayor a 0")
def main():
    #Ejemplo
    #peliculas = {
    #'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    #'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    #}


    #cartelera = {
    #'P101': [5990, 40],
    #'P102': [7990, 0],
    #}


    while True:
        opcion = int(input(leer_op()))