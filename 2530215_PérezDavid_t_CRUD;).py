"""
CRUD in-python
Alumno: David Gerardo Pérez Reyes
Matrícula: 2530215
Grupo: 1M-1

"""
"""
# RESUMEN EJECUTIVO
CRUD (Create, Read, Update, Delete) es un conjunto de operaciones básicas para gestionar datos en aplicaciones.
En Python, estas operaciones se pueden implementar utilizando estructuras de datos como listas o diccionarios.
Este programa proporciona un CRUD simple en memoria para manejar ítems con atributos como id, name, price y quantity, permitiendo al usuario interactuar mediante un menú textual.

"""
"""
Programa CRUD en Python
¿Que es el crud?
Create, Read, Update, Delete
Operaciones basicas para manejar datos en aplicaciones
Implementacion en python usando diccionarios
el programa permite al usuario interactuar mediante un menu textual
cada item tiene atributos como id, name, price y quantity
Buenas Practicas:
1. Validacion de entradas: Asegurar que los datos ingresados por el usuario sean
    del tipo y formato correctos para evitar errores.
2. Manejo de errores: Utilizar bloques try-except para capturar y manejar excepciones.
3. Modularidad: Dividir el código en funciones para cada operación CRUD para mejorar la legibilidad y el mantenimiento.
4. Documentacion: Incluir comentarios y docstrings para explicar la funcionalidad del código.
5. Uso de estructuras de datos adecuadas: Elegir entre listas o diccionarios según las necesidades de acceso y manipulación de datos.
6. Pruebas: Realizar pruebas para asegurar que cada operación CRUD funcione correctamente.

"""

items = {}


def create_item(data, item_id, name, price, quantity):
    """Create a new item if the ID does not already exist."""
    if item_id in data:
        return False

    data[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity,
    }
    return True


def read_item(data, item_id):
    """Return the item with the given ID, or None if not found."""
    return data.get(item_id)


def update_item(data, item_id, name, price, quantity):
    """Update fields of an existing item. Returns True if updated."""
    if item_id not in data:
        return False

    if name is not None:
        data[item_id]["name"] = name

    if price is not None:
        data[item_id]["price"] = price

    if quantity is not None:
        data[item_id]["quantity"] = quantity

    return True


def delete_item(data, item_id):
    """Delete an item by ID. Returns True if deleted."""
    if item_id in data:
        del data[item_id]
        return True
    return False


def list_items(data):
    """Print all items in the data structure."""
    if not data:
        print("Item list is empty.\n")
        return

    print("Item list:")
    for item_id, info in data.items():
        print(f"""
    ID      : {item_id}
    NAME    : {info['name']}
    PRICE   : {info['price']}
    QUANTITY: {info['quantity']}
""")
    print()  # línea en blanco al final


def print_menu():
    print("""
Options:
  1) Create item
  2) Read item by ID
  3) Update item by ID
  4) Delete item by ID
  5) List all items
  0) Exit
""")


def main():
    while True:
        print_menu()
        option = input("Insert an option: ").strip()

        if option not in {"0", "1", "2", "3", "4", "5"}:
            print("Error -> Invalid option.\n")
            continue

        if option == "0":
            print("GOODBYE!")
            break

        # CREATE
        if option == "1":
            print("\n-- CREATE ITEM --\n")
            item_id = input("Insert the item ID: ").strip()
            if not item_id:
                print("Error: invalid ID.\n")
                continue

            name = input("Insert name: ").strip()
            if not name:
                print("Error: name cannot be empty.\n")
                continue

            try:
                price = float(input("Insert the price: "))
                quantity = int(input("Insert the quantity: "))
            except ValueError as error:
                print(f"Error: invalid numeric input -> {error}\n")
                continue

            if price < 0.0 or quantity < 0:
                print("Error: price and quantity cannot be negative.\n")
                continue

            created = create_item(items, item_id, name, price, quantity)
            if created:
                print("\nThe item has been created.\n")
            else:
                print("\nError: ID already exists.\n")

        # READ
        elif option == "2":
            print("\n-- READ ITEM --\n")
            item_id = input("Insert the item ID: ").strip()
            if not item_id:
                print("Error: invalid ID.\n")
                continue

            result = read_item(items, item_id)
            if result is None:
                print("Item not found.\n")
            else:
                print(f"Item found: {result}\n")

        # UPDATE
        elif option == "3":
            print("\n-- UPDATE ITEM --\n")
            item_id = input("Insert the item ID to update: ").strip()
            if not item_id:
                print("Error: invalid ID.\n")
                continue

            name = input("Insert the new name: ").strip()
            try:
                price = float(input("Insert the new price: "))
                quantity = int(input("Insert the new quantity: "))
            except ValueError as error:
                print(f"Error: invalid numeric input -> {error}\n")
                continue

            if price < 0 or quantity < 0:
                print("Error: values cannot be negative.\n")
                continue

            updated = update_item(items, item_id, name, price, quantity)
            if updated:
                print("\nItem updated successfully.\n")
            else:
                print("Update failed: item not found.\n")

        # DELETE
        elif option == "4":
            print("\n-- DELETE ITEM --\n")
            item_id = input("Insert the item ID to delete: ").strip()
            if not item_id:
                print("Error: invalid ID.\n")
                continue

            result = delete_item(items, item_id)
            if result:
                print("The item was successfully deleted.\n")
            else:
                print("Item not found.\n")

        # LIST ALL
        elif option == "5":
            print("\n-- LIST ALL ITEMS --\n")
            list_items(items)


if __name__ == "__main__":
    main()

"""
CONCLUSIONES:
    En conclusión, la implementación de un sistema CRUD en Python utilizando diccionarios demuestra cómo se
    pueden gestionar datos de manera eficiente y estructurada. Al seguir buenas prácticas como la validación de entradas,
    el manejo de errores y la modularidad del código, se mejora la robustez y manten
    Facilidad del programa. Este enfoque no solo facilita la interacción del usuario a través de un menú claro,
    sino que también resalta la importancia de una documentación adecuada y pruebas exhaustivas para asegurar
    el correcto funcionamiento de cada operación CRUD.

"""

"""
REFERENCES:
1. Python Documentation: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
2. Python Input Function: https://www.w3schools.com/python/ref_func_input.asp
3. Exception Handling in Python: https://realpython.com/python-exceptions/
4. Python Functions: https://www.programiz.com/python-programming/function
5. CRUD Operations Explanation: https://www.geeksforgeeks.org/crud-operations-in-python/
"""

"""
Url del repositorio de github:
https://github.com/davidgerardoperez525/U2_CHARLY_HOMEWORK.git
"""