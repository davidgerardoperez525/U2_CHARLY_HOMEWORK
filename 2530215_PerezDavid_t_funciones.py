"""
2530215_PerezDavid_t_funciones.py
Matrícula: 2530215
Grupo: 1M-1
Alumno: David Gerardo Pérez Reyes

#Resumen Ejecutivo:

En este archivo se implementan seis problemas diferentes utilizando funciones en Python. Cada problema aborda una tarea específica, 
desde cálculos geométricos hasta clasificación de calificaciones y manipulación de listas. Se incluyen validaciones de entrada para garantizar que los datos proporcionados sean adecuados para el procesamiento. 
Los problemas están diseñados para cubrir una variedad de conceptos de programación, incluyendo funciones con y sin retorno, manejo de errores, y uso de parámetros opcionales. 
El código está estructurado para ser claro y fácil de entender, con comentarios que explican cada sección y función.


"""
"""

problem 1: Rectangle area and perimeter (function with return values)
Description: Calculate area and perimeter of a rectangle.
Inputs: width (float), height (float)
Outputs: prints "Area:" and "Perimeter:"
Validations: width > 0, height > 0
Test cases:
1) Normal: width=5, height=10 -> Area:50, Perimeter:
30
2) Border: width=0.1, height=0.1 -> Area:0
, Perimeter:0.4
3) Error: width=-5, height=10 -> Error: invalid input
"""

print("\n---------------PROBLEM-#1--------")

def calculate_area (widht, height):
    return widht * height

def calculate_perimeter(widht, heihgt):
    return 2 * (widht+height)


widht = 0 
height = 0

try: 
    widht = float(input("weight: "))
    height = float(input("height: "))

except:
    widht = 0
    height = 0 

if widht <= 0 or height <= 0 : 
    print("Error Invalid input")
else: 
    area = calculate_area(widht, height)
    perimeter = calculate_perimeter(widht, height)
    print(f"area : {area}")
    print(f"perimeter : {perimeter}")


print("\n ---------PROBLEM-#2----------------------")

"""
Problem 2: Score classification function
 Description: Classify score into letter grade. 
    Inputs: score (float)
    Outputs: prints "Score:" and "Category:"
    Validations: 0 <= score <= 100
    Test cases:
    1) Normal: score=85 -> Category:B
    2) Border: score=90 -> Category:A
    3) Error: score=-5 or score=105 -> Error: invalid input


"""
def classify_score(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else : 
        return "F"

try: 
    score =float(input("insert your score: "))
except:
    score = -1

if score < 0 or score > 100:
    print("Error Invalid input")

else: 
    category = classify_score (score)
    print(f" Score {score} \
            Category : {category}")


print ("\n----------PROBLEM-#3-------------")
"""
    Problem 3: Summarize list of numbers (pure function)
    Description: Return min, max, average of a list of numbers.
    Inputs: numbers_list (list of float)
    Outputs: prints "Min:", "Max:", "Average:"
    Validations: numbers_list not empty
    Test cases:
    1) Normal: numbers=[1,2,3,4,5] -> Min:1, Max:5, Average:3
    2) Border: numbers=[10] -> Min:10, Max:10,
    Average:10
    3) Error: numbers=[] -> Error: invalid input   

"""

def summarize_numbers(numbers_list):
    summary = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return summary

numbers_text = input("Insert  separated by commas : ").strip()

if not numbers_text:
    print("error invalid input")
else:
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for part in parts:
            part = part.strip()
            if part == "":
                print("error, the number cannot be null")
            else:
                numbers_list.append(float(part))

        if len(numbers_list) == 0:
            print("Error, the list cannot be null")
        else:
            result = summarize_numbers(numbers_list)
            print(f"Max : {result['max']}")
            print(f"min : {result['min']}")
            print(f"average : {result['average']}")
    except:
        print("invalid input: please insert only numbers")


print ("\n -------PROBLEM-#4-------------")

"""
Problem 4: Apply discount to list of prices
 Description: Apply discount rate to each price in list.
    Inputs: prices_list (list of float), discount_rate (float 0-1)
    Outputs: prints "Original prices:" and "Prices with discount:"
    Validations: prices_list not empty, 0 <= discount_rate < 1
    Test cases:
    1) Normal: prices=[100,200], discount_rate=0.1 -> Prices with discount:[90,180]
    2) Border: prices=[50], discount_rate=0 -> Prices with discount:[
50]
    3) Error: prices=[], discount_rate=0.1 or discount_rate=1.5 -> Error: invalid input
    
"""

def apply_disocunt (prices_list, discount_rate):
    discounted = []
    for prices in prices_list:
        discounted_prices= prices - (prices*discount_rate)
        discounted.append(discounted_prices)
    return discounted

price_text = input("insert prices: ").strip()
discount_text = input("insert discount rate (0 to 1): ").strip()

if not price_text or  not discount_text:
    print("Error: Invalid input, cannot be null")
else: 
    try:
        discount_rate =float(discount_text) 
        if discount_rate >= 0 or discount_rate < 1:
            parts = price_text.split(",")
            prices_list = []
            for part in parts : 
                part = part.strip()
                if part == "":
                    print("Error the number cannot be null")
                else:
                    price = float(part)
                
                if price < 0: 
                    print("Error, the price cannot be negative")
                else:
                    prices_list.append(price)
            if len(prices_list) == 0 :
                print("Error the number list cannot be null")
            else: 
                discounted_list = apply_disocunt(prices_list, discount_rate)
                print(f"Original prices: {prices_list}" )
                print(f"prices with discount: {discounted_list}")
        else:
            print("Error invalid input")

    except Exception as error:
        print("Error Invalid Input")

print("\n---------------PROBLEM-#5----------------")

"""
Problem 5: Greeting function with optional title
 Description: Return greeting with optional title.
    Inputs: user_name (str), user_title (str, optional)
    Outputs: prints "Greeting:"
    Validations: user_name not empty
    Test cases:
    1) Normal: user_name="Alice", user_title="Dr." -> Greeting: Dr. Alice
    2) Border: user_name="Bob", user_title="" -> Greeting: Bob
    3) Error: user_name="" -> Error: invalid input

"""


def greet(UserName="", userTitle=""):
    UserName = UserName.strip()
    userTitle = user_title.strip()

    if not user_title:
        return f"{user_name}"
    else:
        return f"{userTitle} {user_name}"


user_name = input("Insert name: ").strip()
user_title = input("insert title: ").strip()

if not user_name:
    print("invalid input: User name cannot be null")
else:
    try:

        if not user_title:
            full_name = greet(user_name)
        else:
            full_name = greet(user_name, user_title)
        
        print(f"Greeting: {full_name}")

    except Exception as error:
        print(error)


print("\n---------PROBLEM-#6----------------")
"""
Problem 6: Factorial function
 Description: Return factorial of a number.
    Inputs: n (int)
    Outputs: prints "Number:" and "Factorial:"
    Validations: 1 <= n <= 20
    Test cases:
    1) Normal: n=5 -> Factorial:120
    2) Border: n=1 -> Factorial:1
    3) Error: n=0 or n=21 -> Error: invalid input

"""

def factorial_number(n):
    result=1
    for i in range(1 , n+1):
        result = result * i
    return result

number = 0
try: 
    number = int(input("Insert a number (1-20): "))
except:
    number = 0

if number < 1 or number > 20:
    print("Invalid Number: Please insert a number inside the specified range")

else : 
    factorial = factorial_number(number)

    print (f"Number: {number}")
    print (f"Factorial : {factorial}" )
"""
Conclusions:

    en este archivo se han implementado diversas funciones en Python para resolver problemas específicos, demostrando la versatilidad y potencia del lenguaje en la manipulación de datos y cálculos matemáticos.
    Se han abordado temas como validación de entradas, manejo de errores, y uso de parámetros opcionales, lo que es fundamental para desarrollar aplicaciones robustas y confiables.
    La implementación de funciones puras y con retorno ha permitido una mayor modularidad y reutilización del código, facilitando su mantenimiento y comprensión.
    La elección de enfoques iterativos en lugar de recursivos para ciertos problemas, como el cálculo del factorial, destaca la importancia de considerar la eficiencia y las limitaciones del entorno de ejecución al diseñar soluciones.  

 References:

    https://docs.python.org/3/tutorial/index.html
    https://realpython.com/python-functions/
    https://www.w3schools.com/python/
    https://www.geeksforgeeks.org/python-program-to-find-factorial-of-a-number/
    HTTPS://www.programiz.com/python-programming/methods/built-in/min
    https://www.programiz.com/python-programming/methods/built-in/max
"""

"""
Url del repositorio de github:
https://github.com/davidgerardoperez525/U2_CHARLY_HOMEWORK.git

"""