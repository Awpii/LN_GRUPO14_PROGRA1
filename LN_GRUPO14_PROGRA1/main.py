import login
from validaciones import validar_int
from altas import alta_gasto
from bajas import baja_gasto

login = login()

while login == True:
    print("-Menu")
    print("_"*50)
    print("""
    1 - Gastos
    2 - Categorias
    3 - Presupuestos
    4 - Ahorros
    5 - Carga rapida matrices
    0 - Salir
    """)
    opcion = input("Seleccionar opcion: ")
    opcion = validar_int(opcion)
    while opcion == False or opcion < 0 or opcion > 10:
        print("Numero invalido")
        opcion = input("Seleccionar opcion: ")
        opcion = validar_int(opcion)

    if opcion == 1:
        print("=== Gastos ===")
        print("1 - Alta de gasto")
        print("2 - Baja de gasto")
        print("0 - Volver")
        subopcion = input("Seleccione opcion: ")
        subopcion = validar_int(subopcion)

        if subopcion == 1:
            alta_gasto()
        elif subopcion == 2:
            baja_gasto()

    elif opcion == 2:
        print("Categorias (en desarrollo)")
    elif opcion == 3:
        print("Presupuesto (en desarrollo)")
    elif opcion == 4:
        print("Informe (en desarrollo)")
    elif opcion == 5:
        print("Carga Rápida")
        print("Cargando datos de prueba")
        print("Valores de prueba agregados")
    elif opcion == 0:
        login = False
        print("Saliendo")