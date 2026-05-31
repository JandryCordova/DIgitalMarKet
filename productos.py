class Producto:
    def __init__(self, nombre, precio):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")
        
        self.nombre = nombre.strip()
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f}"


class DigitalMarKet:
    def __init__(self):
        self.productos = []

    def registrar_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto: ").strip()
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(nombre, precio)
            self.productos.append(producto)
            print("✅ Producto registrado correctamente.")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception:
            print("❌ Error inesperado al registrar producto.")

    def mostrar_productos(self):
        print("\n=== Productos Registrados ===")
        if not self.productos:
            print("No hay productos registrados.")
        else:
            for producto in self.productos:
                print(producto)

    def menu(self):
        while True:
            print("\n=== DigitalMarKet V2.0.0 ===")
            print("1. Registrar producto")
            print("2. Mostrar productos")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_producto()
            elif opcion == "2":
                self.mostrar_productos()
            elif opcion == "3":
                print("👋 Saliendo del sistema...")
                break
            else:
                print("❌ Opción inválida.")


# Ejecución del sistema
if __name__ == "__main__":
    sistema = DigitalMarKet()
    sistema.menu()
