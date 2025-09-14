<<<<<<< HEAD
# modificacion.py
=======
import re
from validaciones import validar_int
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb
from matriz import Gastos, Categorias

# Estructura esperada de cada gasto:
# (id, fecha, monto, tipo, categoria, descripcion, cuenta_origen, cuenta_destino)

# ---------------------------------------
<<<<<<< HEAD
# Helpers generales (sin 'validaciones' ni 're')
# ---------------------------------------
def _es_fecha_valida_ddmmaaaa(txt):
    """
    Chequeo simple con técnicas vistas en clase:
    - Debe tener 3 partes separadas por '/'
    - Cada parte debe ser numérica
    - Largo: DD(2) / MM(2) / AAAA(4)
    NO valida calendario real (ej. 31/02).
    """
    partes = txt.strip().split("/")
    if len(partes) != 3:
        return False
    d, m, a = partes[0], partes[1], partes[2]
    return (len(d) == 2 and d.isdigit()
            and len(m) == 2 and m.isdigit()
            and len(a) == 4 and a.isdigit())
=======
# Helpers generales
# ---------------------------------------
def _es_fecha_valida_ddmmaaaa(txt):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", txt.strip()))
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb

def _leer_fecha(mensaje="Nueva fecha (DD/MM/AAAA): "):
    f = input(mensaje).strip()
    while not _es_fecha_valida_ddmmaaaa(f):
        print("Formato inválido. Use DD/MM/AAAA.")
        f = input(mensaje).strip()
    return f

def _mostrar_gasto(g):
    print("-"*60)
    print(f"ID: {g[0]} | Fecha: {g[1]} | Monto: {g[2]} | Tipo: {g[3]} | Cat: {g[4]}")
    print(f"Desc: {g[5]} | Origen: {g[6]} | Destino: {g[7]}")
    print("-"*60)

def _buscar_indice_por_id(gid):
    for i, g in enumerate(Gastos):
        if g[0] == gid:
            return i
    return -1

def _leer_id_existente():
    if not Gastos:
        print("No hay gastos cargados.")
        return None
<<<<<<< HEAD
    while True:
        texto = input("Ingrese ID de gasto: ").strip()
        try:
            gid = int(texto)
            break
        except:
            print("ID inválido. Debe ser un número entero.")
=======
    texto = input("Ingrese ID de gasto: ").strip()
    while not re.match(r"^\d+$", texto):
        print("ID inválido. Debe ser un número entero.")
        texto = input("Ingrese ID de gasto: ").strip()
    gid = int(texto)
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb
    idx = _buscar_indice_por_id(gid)
    if idx == -1:
        print(f"No existe gasto con ID {gid}.")
        return None
    return idx

def _seleccionar_tipo():
    print("\nTipo de gasto:")
    print("1 - Fijo")
    print("2 - Variable")
<<<<<<< HEAD
    while True:
        txt = input("Seleccionar tipo (1-2): ").strip()
        try:
            op = int(txt)
            if op in (1, 2):
                return "Fijo" if op == 1 else "Variable"
            else:
                print("Opción inválida. Use 1 o 2.")
        except:
            print("Entrada inválida. Debe ser un número entero.")
=======
    op = validar_int(input("Seleccionar tipo (1-2): "))
    while op is False or op not in (1, 2):
        print("Opción inválida. Use 1 o 2.")
        op = validar_int(input("Seleccionar tipo (1-2): "))
    return "Fijo" if op == 1 else "Variable"
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb

def _armar_dic_categorias():
    """
    Construye {id:int -> nombre:str} a partir de matriz.Categorias.
    Se espera cada fila como [id, nombre, ...]
    """
    dic = {}
    for fila in Categorias:
        if len(fila) >= 2:
            try:
                cid = int(fila[0])
                dic[cid] = str(fila[1])
            except:
                continue
    return dic

def _seleccionar_categoria():
    dic = _armar_dic_categorias()
    if not dic:
        print("No hay categorías cargadas. Se usará 'Sin categoria'.")
        return "Sin categoria"

    print("\nSeleccione una categoría:")
    for cid in sorted(dic.keys()):
        print(f"{cid} - {dic[cid]}")
    print("0 - Sin categoria")

<<<<<<< HEAD
    while True:
        op = input("Ingrese número de categoría: ").strip()
        try:
            num = int(op)
            break
        except:
            print("Opción inválida. Debe ser un número.")

    if num == 0:
        return "Sin categoria"
    if num in dic:
        return dic[num]
=======
    op = input("Ingrese número de categoría: ").strip()
    while not re.match(r"^\d+$", op):
        print("Opción inválida. Debe ser un número.")
        op = input("Ingrese número de categoría: ").strip()

    op = int(op)
    if op == 0:
        return "Sin categoria"
    if op in dic:
        return dic[op]
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb

    print("Categoría inexistente. Se mantiene la actual.")
    return None  # indica no cambiar

# ---------------------------------------
# Operaciones de modificación
# ---------------------------------------
def modificar_monto_por_id():
    print("\n=== Modificar monto ===")
    idx = _leer_id_existente()
    if idx is None:
        return
    g = Gastos[idx]
    _mostrar_gasto(g)

<<<<<<< HEAD
    while True:
        txt = input("Nuevo monto (entero): ").strip()
        try:
            nuevo = int(txt)
            break
        except:
            print("Monto inválido. Debe ser un entero.")
=======
    nuevo = validar_int(input("Nuevo monto (entero): "))
    while nuevo is False:
        print("Monto inválido. Debe ser un entero.")
        nuevo = validar_int(input("Nuevo monto (entero): "))
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb

    # reemplazar tupla completa
    Gastos[idx] = (g[0], g[1], nuevo, g[3], g[4], g[5], g[6], g[7])
    print("Monto actualizado correctamente.")
    _mostrar_gasto(Gastos[idx])

def modificar_descripcion_por_id():
    print("\n=== Modificar descripción ===")
    idx = _leer_id_existente()
    if idx is None:
        return
    g = Gastos[idx]
    _mostrar_gasto(g)

    nueva = input("Nueva descripción (puede ser vacío para '-'): ").strip()
    if nueva == "":
        nueva = "-"
    Gastos[idx] = (g[0], g[1], g[2], g[3], g[4], nueva, g[6], g[7])
    print("Descripción actualizada correctamente.")
    _mostrar_gasto(Gastos[idx])

def modificar_tipo_por_id():
    print("\n=== Modificar tipo (Fijo/Variable) ===")
    idx = _leer_id_existente()
    if idx is None:
        return
    g = Gastos[idx]
    _mostrar_gasto(g)

    nuevo_tipo = _seleccionar_tipo()
    Gastos[idx] = (g[0], g[1], g[2], nuevo_tipo, g[4], g[5], g[6], g[7])
    print("Tipo actualizado correctamente.")
    _mostrar_gasto(Gastos[idx])

def modificar_categoria_por_id():
    print("\n=== Modificar categoría ===")
    idx = _leer_id_existente()
    if idx is None:
        return
    g = Gastos[idx]
    _mostrar_gasto(g)

    nueva_cat = _seleccionar_categoria()
    if nueva_cat is None:
        print("No se realizaron cambios.")
        return
    Gastos[idx] = (g[0], g[1], g[2], g[3], nueva_cat, g[5], g[6], g[7])
    print("Categoría actualizada correctamente.")
    _mostrar_gasto(Gastos[idx])

def modificar_fecha_por_id():
    print("\n=== Modificar fecha ===")
    idx = _leer_id_existente()
    if idx is None:
        return
    g = Gastos[idx]
    _mostrar_gasto(g)

    nueva_fecha = _leer_fecha()
    Gastos[idx] = (g[0], nueva_fecha, g[2], g[3], g[4], g[5], g[6], g[7])
    print("Fecha actualizada correctamente.")
    _mostrar_gasto(Gastos[idx])

def modificar_cuentas_por_id():
    print("\n=== Modificar cuentas (origen/destino) ===")
    idx = _leer_id_existente()
    if idx is None:
        return
    g = Gastos[idx]
    _mostrar_gasto(g)

    nueva_origen = input("Nueva cuenta origen (vacío = '-'): ").strip() or "-"
    nueva_destino = input("Nueva cuenta destino (vacío = '-'): ").strip() or "-"
    Gastos[idx] = (g[0], g[1], g[2], g[3], g[4], g[5], nueva_origen, nueva_destino)
    print("Cuentas actualizadas correctamente.")
    _mostrar_gasto(Gastos[idx])

# ---------------------------------------
<<<<<<< HEAD
# Menú local de modificación (sin validaciones.py)
=======
# Menú local de modificación
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb
# ---------------------------------------
def menu_modificaciones():
    while True:
        print("""
=== MODIFICACIONES ===
1 - Monto
2 - Descripción
3 - Tipo (Fijo/Variable)
4 - Categoría
5 - Fecha
6 - Cuentas (origen/destino)
0 - Volver
""")
<<<<<<< HEAD
        # leer opción solo con int() y try/except
        while True:
            txt = input("Seleccione opción: ").strip()
            try:
                op = int(txt)
                break
            except:
                print("Entrada inválida. Debe ser un número entero.")

        if op < 0 or op > 6:
=======
        op = validar_int(input("Seleccione opción: "))
        if op is False or op < 0 or op > 6:
>>>>>>> feeb1ff61af8cb52f1a15a90958d8829bee85afb
            print("Opción inválida.")
            continue

        if op == 1:
            modificar_monto_por_id()
        elif op == 2:
            modificar_descripcion_por_id()
        elif op == 3:
            modificar_tipo_por_id()
        elif op == 4:
            modificar_categoria_por_id()
        elif op == 5:
            modificar_fecha_por_id()
        elif op == 6:
            modificar_cuentas_por_id()
        elif op == 0:
            break
