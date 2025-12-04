"""
#MANEJO DE LISTAS, TUPLAS Y DICCIONARIOS EN PYTHON
#David Gerardo Pérez Reyes
#Matrícula: 2530215
#Grupo: 1M-1


#RESUMEN EJECUTIVO

Las tuplas y diccionarios son estructuras de datos fundamentales en Python que permiten almacenar y organizar información de manera eficiente.
Las tuplas son colecciones ordenadas e inmutables, ideales para representar datos que no deben cambiar, como coordenadas o registros fijos. Por otro lado, los diccionarios son colecciones desordenadas de pares clave-valor, perfectos para búsquedas rápidas y asociaciones entre datos, como catálogos de productos o libros de contactos.
El uso adecuado de estas estructuras mejora la legibilidad del código y facilita la gestión de datos complejos en aplicaciones diversas.

#BUENAS PRACTICAS
- Utilizar nombres descriptivos para variables y funciones que reflejen su propósito.
- Comentar el código para explicar la lógica y los pasos importantes.
- Validar las entradas del usuario para evitar errores en tiempo de ejecución.
- Manejar excepciones adecuadamente para mejorar la robustez del programa.
- Seguir las convenciones de estilo de Python (PEP 8) para mantener la coherencia en el código.


"""

"""

Problem 1: Shopping list basics (list operations)
Description:
Maneja una lista de compras: agrega un nuevo ítem, cuenta total y busca un ítem.

Inputs:
- initial_items_text (string) e.g. "apple,banana,orange"
- new_item (string)
- search_item (string)
Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false
Validations:
- initial_items_text not empty after strip()
- new_item and search_item not empty after strip()
Test cases:
1) Normal: "apple, banana, orange", new_item="pear", search_item="banana"
2) Border: initial_items_text=" " (empty) -> treat as empty list
3) Error: new_item=" " -> "Error: invalid input"
"""

print("\n-----------------------------PROBLEM-#1----------------")

initial_list = input("Insert the products: ").strip()
new_item = input("Insert the new Item: ").strip()
search_Item = input("Enter the item to search for: ").strip()

if not new_item or not search_Item:
    print("Error the values cannot be null")
else:
    if initial_list == "":
        items = []
    else:
        items = [item.strip() for item in initial_list.split(",") if item.strip()]
    

    items.append(new_item)
    quantity = len(items)
    found_item = search_Item in items

    print(f"""
    item List : {items}
    Total Items : {quantity}
    found item : {found_item}
    """)


print("\n--------------------PROBLEM-#2------------------------")
"""
-----------------------------------------------------------------------------
Problem 2: Points and distances with tuples
Description:
lee dos puntos 2D como tuplas, calcula distancia euclidiana y punto medio.
Inputs:
- x1, y1, x2, y2 (floats)
Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)
Validations:
- Ensure inputs can be converted to float
Test cases:
1) Normal: 0,0 and 3,4 -> distance 5.0 midpoint (1.5,2.0)
2) Border: same point -> distance 0.0
3) Error: non-numeric input -> "Error: invalid input"

"""

point_A = input("Insert the fisrt coordinates: ")
point_B = input("Insert the second coordinates: ")

try:
    point_A_numbers = tuple([float(n) for n in point_A.split(",")])
    point_B_numbers = tuple([float(n) for n in point_B.split(",")])

    distance = ((point_A_numbers[0]-point_B_numbers[0])**2 + (point_A_numbers[1]-point_B_numbers[1])**2)**0.5
    midpoint = ((point_A_numbers[0] + point_B_numbers[0])/2 , (point_A_numbers[1] + point_B_numbers[1])/2)
    print(f"""
    point A: {point_A_numbers}
    point B : {point_B_numbers}
    distance : {distance}
    midpoint : {midpoint}
    """)
except:
    print("Error invalid Input")

"""    
Problem 3: Product catalog with dictionary
Description:
maneja un catálogo de productos con precios usando un diccionario.
Calcula el precio total para una cantidad dada de un producto.
Inputs:
- product_name (string)
- quantity (int)
Outputs:
- If exists: "Unit price:", "Quantity:", "Total:"
- If not: "Error: product not found"
Validations:
- product_name not empty
- quantity > 0 and convertible to int
Test cases:
1) Normal: "apple", 2
2) Border: quantity = 1
3) Error: product not in catalog
"""
print("\n--------------------------------------------")

products = {
    "leche" : 15.0,
    "azucar" : 20,
    "donas" :22.1 
}
product_name = input("Enter the product you wish to purchase: ").strip().lower()
quantity_product = input("how many products? : ").strip().lower()

try:
    quantity_product = int(quantity_product)
    if product_name == "":
        print("Invalid input the name product cannot be null")
    else:
        if product_name in products :
            unit_price =  products[product_name]
            total_price = quantity_product * unit_price

            print(f"""
            unit Price {unit_price}
            quantity_product {quantity_product}
            total {total_price}
            """)
        else: 
            print("Sorry the product not exist")
        
        

        
except:    
    print("Error Invalid Inputs")

print("\n------------PROBLEM-#4---------------------")

"""
Problem 4: Student grades with dict and list
Description:
lee un diccionario de estudiantes y sus calificaciones, calcula promedio y si aprobó.
Inputs:
- student_name (string)
Outputs:
- If exists: "Grades:", "Average:", "Passed:"
- If not: "Error: student not found"
Validations:
- student_name not empty
- Check student exists and grades list not empty
Test cases:
1) Normal: existing student with grades
2) Border: student with single grade = 70 -> passed
3) Error: student not in dict

"""

grades = {
    "Victor" : [100, 100, 90],
    "Paulinho" : [100, 100 ,100],
    "Angel" : [60, 70, 80]  
}

name_estudent = input("Insert the name : ").strip().lower()

if name_estudent == "":
    print("Erro invalid input")
else:
    if name_estudent in grades : 
        estudent_ratings = grades[name_estudent]
        average = sum(estudent_ratings) / len(estudent_ratings)
        passed = average >= 70
        print(f"""
                Estudent : {name_estudent}
                estudent ratings : {estudent_ratings}
                average : {average}
                passed : {passed}
""")
    else: 
        print("The estudent not found")

print("\n-----------PROBLEM-#5----------------------")
"""
Problem 5: Word frequency counter (list + dict)
Description:
cuenta la frecuencia de cada palabra en una oración dada.
Inputs:
- sentence (string)
Outputs:
- "Words list:", "Frequencies:", "Most common word:"
Validations:
- sentence not empty after strip()
- Optionally remove simple punctuation by replacement
Test cases:
1) Normal: "hello charly"
2) Border: oracion con puntuacion
3) Error: vacio
"""

sentence = input("Insert the sentence: ").strip().lower().replace(",", "")
words = {}
sentence = sentence.split()


if not sentence : 
    print("Error Invalid Input")

else:
    for word in sentence:
        words[word] = 0

    for word in sentence:
        if word in words:
            words[word] += 1
    
    frecuent = max(words, key=words.get)
    print(f"""
    words : {sentence}
    frecuencies : {words}
    most common : {frecuent}
""")

print("\n----------------------PROBLEM-#6---------------------------")


"""
Problem 6: Simple contact book (dictionary CRUD)
Description:
implementa un libro de contactos simple con agregar, buscar y eliminar.
Inputs:
- action_text (string: "ADD","SEARCH","DELETE")
- name (string)
- phone (string for ADD)
Outputs:
- "Contact saved:" name, phone
- "Phone:" phone
- "Contact deleted:" name
- "Error: contact not found"
Validations:
- action_text normalized to uppercase and valid
- name and phone not empty where required
Test cases:
1) Normal: ADD new contact, SEARCH it, DELETE it
2) Border: ADD existing contact (update)
3) Error: SEARCH non-existing
"""

contacts = {
    "Paulo" : "8340002130",
    "victor" : "0987654321",
    "anuar": "6562132316"
}

def add(data, name, number):
    if name in data : 
        data[name] = number
        return "Changed contact"
    else:
        data[name] = number
        return "Contact saved"
    
def search_contact(data, name):
    if name in data:
        return data.get(name)
    else : 
        return ("Contact not found")
def delete_contact(data, name):
    if name in data:
        del data[name]
        return "Deleted contact"
    else:
        return "Contact not found"
while True:
    print("""
        Select A option: 
        1) ADD
        2) SEARCH
        3)DELETE
        0)EXIT
        """)
    option = input("Insert A option: ")
    if option == "0":
        break
    elif option == "1":
        print("\n----ADD----")
        name = input("Insert a name to yout contact : ").strip()
        number = input("Insert a number :").strip()
        if not name or not number :
            print("\n The values cannor be null")
            continue
        else:
            add_contact = add(contacts,name,number)
            print(add_contact)

    elif option == "2":
        print("---SEARCH---")
        name = input("Insert a name to search :").strip()
        if not name : 
            print("\n the name cannot be null")
        else:
            search = search_contact(contacts,name)
            print(f"number : {search}")
    
    elif option == "3":
        print("\n---Delete---")
        name = input("Insert a name to yout contact : ").strip()
        if not name : 
            print("\n the name cannot be null")
        else:
            delete = delete_contact(contacts,name)
            print(delete)

"""
"#CONCLUSIONES
El manejo de listas, tuplas y diccionarios en Python es esencial para organizar y manipular datos de manera eficiente.
Las listas son ideales para colecciones ordenadas y mutables, permitiendo agregar, eliminar y modificar elementos fácilmente.
Las tuplas, al ser inmutables, son útiles para datos que no deben cambiar,
como coordenadas o registros fijos.
proporcionando seguridad y optimización en el uso de memoria.
Los diccionarios permiten almacenar datos en pares clave-valor, facilitando búsquedas rápidas y asociaciones entre datos.
El uso adecuado de estas estructuras mejora la legibilidad del código y facilita la gestión de datos comple


References :
    - Documentación oficial de Python sobre listas, tuplas y diccionarios: https://docs.python.org/3/tutorial/datastructures.html
    - Tutorial de W3Schools sobre Python Lists: https://www.w3schools.com/python/python_lists.asp
    - Tutorial de W3Schools sobre Python Tuples: https://www.w3schools.com/python/python_tuples.asp
    - Tutorial de W3Schools sobre Python Dictionaries: https://www.w3schools.com/python/python_dictionaries.asp
    - Real Python Guide to Python Data Structures: https://realpython.com/python-data-structures/jos en aplicaciones diversas.
"""

"""
Url del repositorio de github:
https://github.com/davidgerardoperez525/U2_CHARLY_HOMEWORK.git
"""