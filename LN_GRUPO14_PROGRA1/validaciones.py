def validar_int(x):
    if x == "-1":
        return int(x)
    #lee si cada elemento es un valor numerico
    if x.isnumeric():
        return int(x)
    #devuelve invalido en caso contrario
    else:
        return False