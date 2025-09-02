def login():
    nombre = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    correct_nombre = "admin"
    correct_contra = "1234"

    if nombre == correct_nombre and contraseña == correct_contra:
        print(f"\nEl inicio de sesión fue exitoso. Bienvenido, {nombre}.")
    else:
        print("\nEl nombre de usuario o contraseña ingresados son incorrectos. Intente nuevamente.")
