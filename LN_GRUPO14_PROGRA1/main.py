import login
from validaciones import validar_int


#Programa principal
login = login()


    

while login == True:
    print("\n-Menu")
    print("_"*50)
    print("""
    1 - Gastos
    2 - Categorias
    3 - Presupuestos
    4 - Ahorros
    5- Carga rapida matrizes
    0 - Salir
    """)
    opcion = input("seleccionar opcion: ")
    opcion = validar_int(opcion)
    while opcion < 0 or opcion > 10 or opcion == False:
        print("numero invalido")
        opcion = input("seleccionar opcion: ")
        opcion = validar_int(opcion)
    print("\n")
    if opcion == 1:
        print("Gastos")
    elif opcion == 2:
        print("Categorias")
    elif opcion == 3:
        print("Presupuesto")
    elif opcion == 4:
        print("Informe")
    elif opcion == 5:
        print("Carga Rapida")
        print("Cargando datos de prueba...\n")
        print("Valores de prueba agregados")
    elif opcion == 0:
        login = False






















































"""def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(f"{col:<20}", end="")
        print()
    print("\n")

def get_categorias():
    categorias = [
        ["id_cat", "categoria", "subcategoria", "Descripcion"],
        [1, "Interbanking", "Transferencias a bancos", "Paso de banco hipotecario a BBVA"],
        [2, "Hogar", "Servicios", "Pago de internet"],
        [3, "Ocio", "Restaurantes", "Cena en restaurante"],
        [4, "Salud", "Gimnasio", "Suplementos GYM"],
        [5, "Transporte", "Pases", "Recarga Sube"],
        [6, "Otros", "Adicciones", "Gramo de Flores"]
    ]
    return categorias

def create_movimientos():
    return [["id_mov", "fecha", "monto", "Tipo_mov", "categoria", "Descripcion", "Cuenta_origen", "Cuenta_destino"]]

def add_expense(movimientos, categorias):
    id_mov = len(movimientos)

    fecha = input("Ingrese la fecha (MM/DD/YYYY): ")
    monto = input("Ingrese el monto: ")
    tipo_mov = input("Ingrese el tipo de movimiento (Gasto/Transferencia): ")

    print("\nSeleccione la categoría:")
    for cat in categorias[1:]:
        print(f"{cat[0]} - {cat[1]} ({cat[2]})")

    cat_id = int(input("Ingrese el número de categoría: "))

    categoria = "Desconocido"
    for cat in categorias[1:]:
        if cat[0] == cat_id:
            categoria = cat[1]

    descripcion = input("Ingrese la descripción: ")
    cuenta_origen = input("Ingrese la cuenta origen (o '-' si no aplica): ")
    cuenta_destino = input("Ingrese la cuenta destino (o '-' si no aplica): ")
    movimientos.append([id_mov, fecha, monto, tipo_mov, categoria, descripcion, cuenta_origen, cuenta_destino])

    print("\n Movimiento agregado correctamente!\n")

def main():
    categorias = get_categorias()
    movimientos = create_movimientos()
    add_expense(movimientos, categorias)
    add_expense(movimientos, categorias)
    print("\n=== Movimientos registrados ===")
    print_matrix(movimientos)

main()
"""