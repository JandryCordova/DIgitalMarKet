productos = []

while True:
    print("\n=== DigitalMarKet ===")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ").strip()

        if nombre == "":
            print("Error: El nombre del producto no puede estar vacío.")
        else:
            productos.append(nombre)
            print("Producto registrado correctamente.")

    elif opcion == "2":
        print("\n=== Productos Registrados ===")

        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print("-", producto)

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")