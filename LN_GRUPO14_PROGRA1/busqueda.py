import re
from validaciones import validar_int
from matriz import Gastos, Categorias

# ---------------------------------------
# Utilitarios de fechas y salida
# ---------------------------------------
def _es_fecha_valida_ddmmaaaa(txt):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", txt.strip()))

def _leer_fecha(mensaje):
    f = input(mensaje).strip()
    while not _es_fecha_valida_ddmmaaaa(f):
        print("Formato inválido. Use DD/MM/AAAA.")
        f = input(mensaje).strip()
    return f

def _fecha_a_tuple(fecha_ddmmaaaa):
    # "DD/MM/AAAA" -> (AAAA, MM, DD) para comparar correctamente
    d, m, a = fecha_ddmmaaaa.split("/")
    return (int(a), int(m), int(d))

def _mostrar_resultados(lista):
    """
    Muestra una tabla simple de gastos.
    Devuelve la cantidad encontrada.
    """
    if not lista:
        print("\nNo se encontraron resultados.")
        return 0

    print("\nResultados:")
    print("-"*80)
    print("ID  | Fecha       | Monto   | Tipo      | Categoria         | Descripción")
    print("-"*80)
    for g in lista:
        gid = g[0]
        fecha = g[1]
        monto = g[2]
        tipo = g[3]
        cat = g[4]
        desc = g[5]
        print(f"{gid:>3} | {fecha:<10}  | {monto:>7} | {tipo:<8} | {cat:<16} | {desc}")
    print("-"*80)
    print(f"Total encontrados: {len(lista)}")
    return len(lista)

# ---------------------------------------
# Búsquedas
# ---------------------------------------
def buscar_por_rango_fechas():
    """
    Pide fecha DESDE y HASTA (DD/MM/AAAA) y filtra Gastos en ese rango (inclusive).
    """
    if not Gastos:
        print("No hay gastos cargados.")
        return

    print("\n=== Búsqueda por rango de fechas ===")
    f_desde = _leer_fecha("Fecha DESDE (DD/MM/AAAA): ")
    f_hasta = _leer_fecha("Fecha HASTA (DD/MM/AAAA): ")

    t_desde = _fecha_a_tuple(f_desde)
    t_hasta = _fecha_a_tuple(f_hasta)
    if t_desde > t_hasta:
        print("Advertencia: DESDE > HASTA. Se intercambian valores.")
        t_desde, t_hasta = t_hasta, t_desde

    resultado = []
    for g in Gastos:
        t = _fecha_a_tuple(g[1])
        if t_desde <= t <= t_hasta:
            resultado.append(g)

    _mostrar_resultados(resultado)

def _armar_dic_categorias():
    """
    Construye {id:int -> nombre:str} a partir de matriz.Categorias.
    Si no hay categorías válidas, devuelve {}.
    Se espera cada fila como [id, nombre, ...]
    """
    dic = {}
    for fila in Categorias:
        if len(fila) >= 2:
            try:
                cid = int(fila[0])
            except:
                continue
            dic[cid] = str(fila[1])
    return dic

def buscar_por_categoria():
    """
    Permite elegir una categoría (por ID) y muestra los gastos que la tengan.
    Si no hay categorías, ofrece buscar 'Sin categoria'.
    """
    if not Gastos:
        print("No hay gastos cargados.")
        return

    print("\n=== Búsqueda por categoría ===")
    dic = _armar_dic_categorias()

    if not dic:
        print("No hay categorías cargadas. ¿Buscar 'Sin categoria'?")
        resp = input("s/n: ").strip().lower()
        if resp == "s":
            filtrados = [g for g in Gastos if g[4] == "Sin categoria"]
            _mostrar_resultados(filtrados)
        else:
            print("Operación cancelada.")
        return

    print("\nSeleccione una categoría:")
    for cid in sorted(dic.keys()):
        print(f"{cid} - {dic[cid]}")
    print("0 - Sin categoria")

    op = input("Ingrese número de categoría: ").strip()
    while not re.match(r"^\d+$", op):
        print("Opción inválida. Debe ser un número.")
        op = input("Ingrese número de categoría: ").strip()

    op = int(op)
    if op == 0:
        nombre_cat = "Sin categoria"
    elif op in dic:
        nombre_cat = dic[op]
    else:
        print("Categoría inexistente.")
        return

    filtrados = [g for g in Gastos if g[4] == nombre_cat]
    _mostrar_resultados(filtrados)

def buscar_por_monto():
    """
    Filtra por rango de monto [min, max]. Ambos inclusive.
    Si se deja vacío alguno, se interpreta como sin límite.
    """
    if not Gastos:
        print("No hay gastos cargados.")
        return

    print("\n=== Búsqueda por monto ===")
    txt_min = input("Monto mínimo (entero, vacío = sin mínimo): ").strip()
    txt_max = input("Monto máximo (entero, vacío = sin máximo): ").strip()

    min_ok = validar_int(txt_min) if txt_min != "" else None
    max_ok = validar_int(txt_max) if txt_max != "" else None

    if txt_min != "" and min_ok is False:
        print("Mínimo inválido.")
        return
    if txt_max != "" and max_ok is False:
        print("Máximo inválido.")
        return

    mmin = min_ok if txt_min != "" else None
    mmax = max_ok if txt_max != "" else None

    resultado = []
    for g in Gastos:
        monto = g[2]
        if (mmin is None or monto >= mmin) and (mmax is None or monto <= mmax):
            resultado.append(g)

    _mostrar_resultados(resultado)

def buscar_por_texto_en_descripcion():
    """
    Busca coincidencia (case-insensitive) en la descripción.
    """
    if not Gastos:
        print("No hay gastos cargados.")
        return

    print("\n=== Búsqueda por texto en descripción ===")
    patron = input("Ingrese texto a buscar: ").strip().lower()
    if patron == "":
        print("Texto vacío. Operación cancelada.")
        return

    resultado = []
    for g in Gastos:
        desc = str(g[5]).lower()
        if patron in desc:
            resultado.append(g)

    _mostrar_resultados(resultado)

# ---------------------------------------
# Menú local de búsqueda (opcional)
# ---------------------------------------
def menu_busquedas():
    """
    Menú simple para encadenar búsquedas desde el programa principal.
    """
    while True:
        print("""
=== BUSQUEDAS ===
1 - Por rango de fechas
2 - Por categoría
3 - Por monto
4 - Por texto en descripción
0 - Volver
""")
        op = validar_int(input("Seleccione opción: "))
        if op is False or op < 0 or op > 4:
            print("Opción inválida.")
            continue
        if op == 1:
            buscar_por_rango_fechas()
        elif op == 2:
            buscar_por_categoria()
        elif op == 3:
            buscar_por_monto()
        elif op == 4:
            buscar_por_texto_en_descripcion()
        elif op == 0:
            break
