
#Manejo de Bucles en Python
# David Gerardo Pérez Reyes
# Matrícula: 2530215
# Grupo: 1M-1

 
"""
#RESUMEN EJECUTIVO:
los bucles son estructuras fundamentales en la programación que permiten repetir bloques de código bajo ciertas condiciones. En Python, los bucles "for" y "while" son las herramientas principales para este propósito.

#BUENAS PRACTICAS:

1. Claridad y legibilidad: Utiliza nombres descriptivos para variables y funciones dentro de los bucles.
2. Evita bucles infinitos: Asegúrate de que las condiciones de los
   bucles "while" eventualmente se vuelvan falsas.
3. Usa "break" y "continue" con moderación: Estos pueden mejorar la legibilidad, pero su uso excesivo puede complicar el flujo del bucle.
4. Comentarios: Documenta la lógica del bucle, especialmente si es compleja.
5. Optimización: Considera la eficiencia del bucle, especialmente con grandes conjuntos de datos.
6. Pruebas: Verifica que los bucles funcionen correctamente con diferentes escenarios de entrada.


"""
"""
---------------------------
Problem 1: Sum of range with for
Description: calcula el total y la suma de números pares desde 1 hasta n.
Inputs:
- n (int)
Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>
Validations:
- n must be convertible to int and n >= 1
- On invalid input: print "Error: invalid input"
Test cases:
Normal: n = 10 -> Sum 55, Even sum 30
Border: n = 1 -> Sum 1, Even sum 0
Error: n = 0 -> Error

"""
print("\n--------------PROBLEM-#1----------------------")

n = input("Insert A number : ").strip()
try:
    n = int(n)
    sum = 0
    even_sum = 0

    for i in range(n+1):
        sum += i

        if i % 2 == 0:
            even_sum += i
    
    print(f"""
additions = {sum}
Even sum = {even_sum}
""")
except:
    print("Error invalid input")

print("\n--------PROBLEM-#2----------------------------")
"""
Problem 2: Multiplication table with for
Description: imprime la tabla de multiplicar de una base hasta un límite m.
Inputs:
- base (int)
- m (int)
Outputs:
- Lines like: "5 x 1 = 5"
Validations:
- base and m convertible to int, m >= 1
- On invalid input: print "Error: invalid input"
Test cases:
1) Normal: base=5, m=4 -> lines for 1..4
2) Border: base=2, m=1 -> one line
3) Error: base=3, m=0 -> Error
"""


try:

    base = int(input("Insert the base: "))
    m = int(input("Insert the limit of the multiplication table: "))

    for i in range (1, m+1):
        print(f"{base} * {i} = {i*base}")

except:
    print("Error invalid input")

print("\n---------------PROBLEM-#3--------")
"""

Problem 3: Average of numbers with while and sentinel
Description: lee números hasta el centinela -1 y calcula el promedio.
Inputs:
- a list of input values (strings or numbers). Sentinel is -1.
Outputs:
- "Count:" <count>
- "Average:" <average_value>
- If no valid data -> "Error: no data"
Validations:
- Each value must be convertible to float (except sentinel handling)
Test cases:
1) Normal: [1.0, 2.0, 3.0, -1] -> Count:3 Average:2.0
2) Border: [-1] -> Error: no data
3) Error: ["a", -1] -> "Error: invalid input"""


number = ""
numbers = []

while number != "-1":
    number = input("\nInsert a Number: ").strip()

    if number == "-1" and not numbers:
        print("Error: No Data")
        break

    if number == "-1":
        print("Exit")
        break
    try:
        float(number)   
    except ValueError:
        print("Error: Solo se permiten números.")
        continue
    numbers.append(number)
try:
    numbers_float = [float(n) for n in numbers]

    addition = sum(numbers_float)
    average = addition / len(numbers_float)

    print(f"""
    addition: {addition}
    average: {average}
    """)
except:
    print("No Data")
print("\n-----------PROBLEM-#4-------------------------")
"""
Problem 4: Password attempts with while
Description: el usuario tiene un número limitado de intentos para ingresar la contraseña correcta.
Inputs:
- a list of attempted passwords (strings) - simulations of user input
Outputs:
- "Login success" on success
- "Account locked" if attempts exhausted
Validations:
- MAX_ATTEMPTS is a positive integer
Test cases:
1) Normal: attempts: ["wrong","admin123"] -> Login success (on second try)
2) Border: attempts: ["admin123"] -> Login success (first try)
3) Error: attempts exhausted without correct password -> Account locked
"""


MAX_ATTEMPS = 5
password = "Admin_1234"
counter = 0

while counter < MAX_ATTEMPS: 
        pin = input("Insert your pin: ")
        if (password == pin):
            print("WELCOME")
            break
        
        else : 
            print("Incorrect PIN")
            counter+=1
            remaining_attemps= MAX_ATTEMPS - counter
        
        if remaining_attemps > 0 :
            print(f"Incorrect pin : {remaining_attemps}")
        else:
            print("You have exceeded the maximum number of attempts. Your account has been blocked.")
print("\n------PROBLEM-#5------------------------------")
"""

# Problem 5: Simple menu with while
 Description: simple menu con option de saludo, mostrar e incrementar contador, y salir.

Inputs:
una lista de opciones (strings) - simulaciones de entrada del usuario

Outputs:
- prints messages according to options. For batch mode, function returns the concatenated log.

 Validations:
 - options must be convertible to int and in {0,1,2,3}

Test cases:
Normal: ["1","3","2","0"] -> Hello! then Counter incremented then Counter:1 then Bye!
Border: ["0"] -> Bye!
Error: ["9","0"] -> Error: invalid input! 

 """
counter_menu = 0

while True:
    try:
        print("""
             1 : Greeting
             2: show counter
             3: increment counter,
             0: Exit
""")
        option = int(input("Selec One Option :"))
    except:
        print("Error invalid input")
        continue

    if option == 0:
        print("bye bye ^^")
        break
    elif option == 1:
        print("HIIIII!!!1")
    elif option == 2:
        print(f"counter : {counter_menu}")
    elif option == 3:
        print("Counter incremented succefully")
        counter_menu += 1
    else:
        print("Error: invalid option")



print("\n------------PROBLEM-#6------------------------")
"""

Problem 6: Pattern printing with nested loops
Description: imprime un patrón de asteriscos en forma de triángulo creciente y opcionalmente invertido.

Inputs:

- n (int)
Outputs:

- lines containing 1..n asterisks
- optional inverted pattern after
Validations:

- n convertible to int and n >= 1
Test cases:

1) Normal: n=4 -> lines: *,**,***,****
2) Border: n=1 -> *
3) Error: n=0 -> Error"""

try:
    n = int(input("Insert the quantity to the triangle : ").strip())

    if n > 0: 
        for i in range(1,n+1):
                print("*" * i)
        
        for i in range(n-1, 0, -1): #Lo hice nomas pa que vea que hay nivel,  y porque esta bien facil
            print("*" * i)
    else : 
        print("Error INvalid Input")
except:
    print("Error Invalid Inpuy")

"""
Conclusiones:
El uso de bucles en Python es esencial para manejar tareas repetitivas de manera eficiente.
La comprensión de las estructuras de bucles "for" y "while", junto con las buenas prácticas en su implementación, permite escribir código claro, eficiente y fácil de mantener. Además, la validación adecuada de entradas y la gestión de errores son cruciales para garantizar la robustez de los programas que utilizan bucles.
usar bucles de manera efectiva puede mejorar significativamente la funcionalidad y la experiencia del usuario en aplicaciones de software.
mas allá de la simple repetición, los bucles permiten la creación de patrones complejos y la manipulación dinámica de datos, lo que es fundamental en el desarrollo de soluciones de programación avanzadas.

Referencias:
https://docs.python.org/3/tutorial/controlflow.html#for-statements
https://realpython.com/python-loops/
https://www.w3schools.com/python/python_for_loops.asp
https://www.programiz.com/python-programming/while-loop
https://www.geeksforgeeks.org/python-loops/
# """

"""
Url del repositorio de github:
https://github.com/davidgerardoperez525/U2_CHARLY_HOMEWORK.git
"""