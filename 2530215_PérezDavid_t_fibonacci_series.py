"""
#Fibonacci Series using Loop in Python
Alumno: David Gerardo Pérez Reyes
Matrícula: 2530215
Grupo: 1M-1

 
"""
"""
Resumen ejecutivo:
    En este archivo se implementa la serie de Fibonacci utilizando un bucle en Python.
    la serie de Fibonacci es una secuencia de números donde cada número es la suma de los dos anteriores, comenzando típicamente con 0 y 1.
    El programa solicita al usuario que ingrese el número de términos que desea generar en la serie y luego calcula y muestra cada término de la serie hasta el número especificado.
    con un rango de validaciones para asegurar que la entrada del usuario sea adecuada para el procesamiento.
"""
"""
    PROGRAM DESCRIPTION
    This program generates the Fibonacci series up to a user-defined number of terms (n).
    It uses a loop to calculate and print each term in the series.
    INPUTS: n (int) - number of terms in the Fibonacci series
    OUTPUTS: Prints the Fibonacci series up to n terms
    VALIDATIONS: n should be a positive integer (n > 0)
    TEST CASES:
    1) Normal: n=7 -> Output: 0, 1,
    1, 2, 3, 5, 8
    2) Border: n=1 -> Output: 0
    3) Error: n=0 -> Output: Error: Invalid Input

"""


try:
    n = int(input("Insert a number: "))

    if n < 1 or n > 50:
        print("put a number between 1 and 50")
    else: 
        a = 0
        b = 1

        for i in range(n):
            c  = a
            print (c)
            a = b
            b  = a + c
except:
    print("Invalid input: ERROR")

"""
 CONCLUSIONES:
    En conclusión, la implementación de la serie de Fibonacci utilizando un bucle en Python demuestra cómo se pueden generar secuencias numéricas de manera eficiente y clara.
    El uso de un bucle permite calcular cada término de la serie de forma iterativa, evitando la sobrecarga de llamadas recursivas y mejorando el rendimiento del programa.
    Además, la inclusión de validaciones de entrada asegura que el programa maneje adecuadamente los casos de error, proporcionando una experiencia de usuario más robusta.
    En resumen, este enfoque no solo facilita la comprensión de la serie de Fibonacci, sino que también destaca las mejores prácticas en la programación, como la validación de entradas y la claridad del código.
 
"""

"""
 REFERENCES:
1. Python Documentation: https://docs.python.org/3/tutorial/controlflow.html#for-statements
2. Fibonacci Series Explanation: https://www.geeksforgeeks.org/python-program-for-fibonacci
3. Error Handling in Python: https://realpython.com/python-exceptions/
4. Python Input Function: https://www.w3schools.com/python/ref_func_input.asp
5. Looping Techniques in Python: https://www.programiz.com/python-programming/for-loop


"""

"""
GITHUB REPOSITORY:
https://github.com/davidgerardoperez525/U2_CHARLY_HOMEWORK.git


"""