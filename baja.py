def baja(movimientos):
    id_baja = int(input("Ingrese el ID del movimiento que desea dar de baja: "))
    encontrado = 0
    for movimiento in movimientos:
        if movimiento[0] == id_baja and movimiento[3] == "activo":
            movimiento[3] = "baja"
            print(f"Movimiento {id_baja} fue dado de baja correctamente.")
            encontrado += 1
            break 
    if encontrado == 0:
        print("El movimiento ingresado no fue encontrado o ya estaba dado de baja. ")

