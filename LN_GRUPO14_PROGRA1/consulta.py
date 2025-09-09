import re
from validaciones import validar_int
from matriz import Gastos

def _mostrar_linea(g):
    # esperado: (id, fecha, monto, tipo, categoria, desc, cuenta_origen, cuenta_destino)
    gid = g[0]
    fecha = g[1]
    monto = g[2]
    tipo = g[3]
    cat = g[4]
    desc = g[5]
    print(f"{gid:>3} | {fecha:<10}  | {monto:>7} | {tipo:<8} | {cat:<16} | {desc}")

def listar_todos():
    """
    Muestra todos los gastos con un formato de tabla simple.
    """
    print("\n=== Consulta: listar todos ===")
    if not Gastos:
        print("No hay gastos cargados.")
        return

    print("-"*80)
    print("ID  | Fecha       | Monto   | Tipo      | Categoria         | Descripción")
    print("-"*80)
    for g in Gastos:
        _mostrar_linea(g)
    print("-"*80)
    print(f"Cantidad: {len(Gastos)}")

def detalle_por_id():
    """
    Pide un ID y muestra todos los campos del gasto si existe.
    """
    print("\n=== Consulta: detalle por ID ===")
    if not Gastos:
        print("No hay gastos cargados.")
        return

    txt = input("Ingrese ID: ").strip()
    while not re.match(r"^\d+$", txt):
        print("ID inválido.")
        txt = input("Ingrese ID: ").strip()
    buscado = int(txt)

    encontrado = None
    for g in Gastos:
        if g[0] == buscado:
            encontrado = g
            break

    if encontrado is None:
        print(f"No existe gasto con ID {buscado}.")
        return

    g = encontrado
    print("\nDetalle:")
    print("-"*40)
    print(f"ID: {g[0]}")
    print(f"Fecha: {g[1]}")
    print(f"Monto: {g[2]}")
    print(f"Tipo: {g[3]}")
    print(f"Categoría: {g[4]}")
    print(f"Descripción: {g[5]}")
    print(f"Cuenta origen: {g[6]}")
    print(f"Cuenta destino: {g[7]}")
    print("-"*40)

def total_general():
    """
    Suma todos los montos y muestra el total.
    """
    print("\n=== Consulta: total general ===")
    total = 0
    for g in Gastos:
        total += g[2]
    print(f"Total de gastos: ${total}")

def totales_por_categoria():
    """
    Suma de montos agrupada por categoría, mostrando de mayor a menor.
    """
    print("\n=== Consulta: totales por categoría ===")
    if not Gastos:
        print("No hay gastos cargados.")
        return

    acum = {}  # {categoria: total}
    for g in Gastos:
        cat = g[4]
        monto = g[2]
        if cat not in acum:
            acum[cat] = 0
        acum[cat] += monto

    # ordenar por total desc
    orden = sorted(acum.items(), key=lambda x: x[1], reverse=True)

    print("-"*40)
    print("Categoria           | Total")
    print("-"*40)
    for cat, total in orden:
        print(f"{cat:<20} | {total:>8}")
    print("-"*40)

def resumen_por_tipo():
    """
    Total por 'Fijo' y 'Variable'.
    """
    print("\n=== Consulta: resumen por tipo ===")
    fijo = 0
    variable = 0
    for g in Gastos:
        if g[3] == "Fijo":
            fijo += g[2]
        elif g[3] == "Variable":
            variable += g[2]

    print("-"*30)
    print(f"Fijo:     ${fijo}")
    print(f"Variable: ${variable}")
    print(f"Total:    ${fijo + variable}")
    print("-"*30)

# ---------------------------------------
# Menú local de consulta (opcional)
# ---------------------------------------
def menu_consultas():
    """
    Menú simple para encadenar consultas desde el programa principal.
    """
    while True:
        print("""
=== CONSULTAS ===
1 - Listar todos
2 - Detalle por ID
3 - Total general
4 - Totales por categoría
5 - Resumen por tipo (Fijo/Variable)
0 - Volver
""")
        op = validar_int(input("Seleccione opción: "))
        if op is False or op < 0 or op > 5:
            print("Opción inválida.")
            continue

        if op == 1:
            listar_todos()
        elif op == 2:
            detalle_por_id()
        elif op == 3:
            total_general()
        elif op == 4:
            totales_por_categoria()
        elif op == 5:
            resumen_por_tipo()
        elif op == 0:
            break
