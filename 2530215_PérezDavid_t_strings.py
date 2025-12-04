# Manejo de strings en Python
#David Gerardo Pérez Reyes
#Matricula: 2530215
#Grupo 1M-1

"""
                        - RESUMEN EJECUTIVO

¿Qué es un string en Python?

   - Un string en Python es una secuencia de caracteres encerrada entre comillas simples ('...') o dobles ("...").
   - Se utiliza para representar texto, como palabras, frases o cualquier combinación de caracteres.
   - Los strings son inmutables, lo que significa que no se pueden cambiar una vez creados; cualquier operación que modifique un string genera uno nuevo.

¿Por qué es importante validar y normalizar texto de entrada ?

Validar y normalizar el texto de entrada, como correos electrónicos, nombres y contraseñas, es fundamental porque permite que los datos que ingresan a un sistema sean correctos, seguros y uniformes. 
La validación ayuda a comprobar que la información cumple con un formato adecuado, por ejemplo, que un correo tenga el símbolo @ o que una contraseña tenga la longitud y complejidad necesarias, lo que evita errores en el funcionamiento del sistema. Además, es una medida clave de seguridad,
ya que reduce el riesgo de ataques informáticos como la inyección de código malicioso.

    - ¿Qué cubrira este documento? 
Este documento contendra: Descripción de cada problema, diseño de entradas y salidas, validaciones aplicadas y uso de métodos de string con casos de prueba (incluyendo el código).
  
# PRINCIPIOS Y BUENAS PRÁCTICAS

 Los strings son inmutables: cualquier cambio genera una nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego el formato.
- Escribir código legible: nombres de variables claros y mensajes de error entendibles.
"""

""" 
# Problem 1: Full name formatter 

   - Descripción: 
El pide al usuario que escriba su nombre completo y se encarga de limpiarlo, corrigiendo mayúsculas, minúsculas 
y espacios de más para dejarlo presentable. Ademas verifica que el usuario haya ingresado un nombre válido con 
al menos dos palabras. Después, muestra el nombre ya formateado en un estilo claro y profesional, y finalmente genera automáticamente 
las iniciales correspondientes.

- Inputs:
   - full_name # Nombre ingresado por el usuario

- Outputs:
   - Name in Title Case: El nombre completo formateado en estilo Title Case.
   - The Initials are: Las iniciales del nombre completo.

- Validations:
   - if full_name == "": # Verifica que el nombre que se ingreso no sea texto en blanco.
   - if len(parts) < 2: # Verifica que el usuario haya ingresado al menos dos nombres.
      
 - Test:
 
   # CASO NORMAL
   What is your name?: david gerardo pérez reyes
   Name in Title Case: David Gerardo Pérez Reyes
   The Initials are: D.G.P.R.
      
   # CASO BORDE
   What is your name?: david
   Error: invalid input, you only enter one name

   # CASO ERROR
   What is your name?:
   Error: invalid input, thats not a name
"""
print("----------------------PROBLEM-#1---------------------------------------------------")

full_name= input("Enter ur name: ")
full_name= full_name.lower().strip()
if full_name == "":
    print("Error: invalid input, thats not a name")
    exit()
parts= full_name.split()
if len(parts) < 2:
    print("Error: invalid input, there is only one name")
    exit()

full_name= " ".join(parts)
full_name= full_name.title()
print("Name in Title Case: ", full_name)

initials= ""
for name in parts:
    initial= name[0].upper()
    initials += initial + "."

print("Initials are: ", initials)
    

"""
# Problem 2: Simple email validator and domain extractor
   - Descripción: 
      Este programa verifica si un correo electrónico ingresado por el usuario es válido según ciertas reglas básicas. 
      Primero, comprueba que el correo contenga exactamente un símbolo "@" y que no tenga espacios en blanco. 
      Luego, extrae la parte del dominio que sigue al "@" y verifica que contenga al menos un punto ".". 
      Si todas las validaciones se cumplen, indica que el correo es válido y muestra el dominio; de lo contrario, informa que no es válido.

   - Inputs:
   - email_text = input("Set your email: ").-  String ingresado por el usuario.

   - Outputs:
   - Valid email: True, Valid email: False .- Indica si el correo es válido o no.
   - print("The domain is:", domain).- Muestra el dominio extraído si el correo es válido.

   - Validations:
   - email_text.count("@") == 1 .- Valida que el correo solo contenga un arroba.
   - " " not in email_text .- Valida que el correo no contenga espacios en blanco.
   - "." in domain .- Valida que tenga un "." en el dominio después del arroba.
  
   - Test Cases: 
      # CASO NORMAL

      Set your email: perez@upv.mx
      Valid email: True
      The domain is: upv.mx
      
      # CASO BORDE

      Set your email: a@b.c
      Valid email: True
      The domain is: b.c

      # CASO ERROR

      Set your email: davidgmail.com
      Valid email: False

"""
print("\n")
print("------------------------------PROBLEM-#2------------------------------------------------------------------------")

email_text= input("Enter a email: ")

if email_text.count("@") == 1 and " " not in email_text:
   at= email_text.find("@")
   domain= email_text[at+1:]
   if "." in domain:
      print("Valid email: True")
      print("The domain is:", domain)
   else:
      print("Valid email: False")

else:
    print("Valid email: False")

"""
# Problem 3: Palindrome checker 

   - Descripción: 
      Este programa verifica si una frase ingresada por el usuario es un palíndromo. 
      Primero, normaliza la frase eliminando espacios y convirtiéndola a minúsculas. 
      Luego, compara la frase normalizada con su reverso. Si son iguales y la longitud de la frase es mayor a 3, 
      indica que es un palíndromo y muestra la frase normalizada; de lo contrario, informa que no lo es.

   - Inputs:
      - phrase .- String ingresado por el usuario mediante input("Type the phrase you wanna check: ").

   - Outputs:
      - "Is palindrome: True" si la frase normalizada es igual a su reverso.
      - "Is palindrome: False" si no es palíndromo o si no cumple la longitud.
      - "Normalized phrase: <phrase>" solo si es palíndromo.

   - Validations:
      - if len(phrase) > 3: .- Si no se cumple al momento de normalizar automaticamente se contempla como palíndromo.

  
   - Test Cases: 
      # CASO NORMAL

      Type the phrase you wanna check: Reconocer
      Is palindrome: True
      Normalized phrase:  reconocer

      
      # CASO BORDE

      Type the phrase you wanna check: metodologias
      Is palindrome: False


      # CASO ERROR

      Type the phrase you wanna check: Hola charly
      Is palindrome: False


"""
print("\n")
print("----------------------------------PROBLEM-#3--------------------------------------------------------------------")

phrase= input("Type the phrase you wanna check: ")
phrase= phrase.replace(" ","").lower()
reverse= phrase[::-1]
if len(phrase) > 3:

   if reverse == phrase:
      print("Is palindrome: True")
      print("Normalized phrase: ", phrase)

   else:
      print("Is palindrome: False")
      
else:
   print("Is palindrome: False")

"""
# Problem 4: Sentence word stats 

   - Descripción: 
      Este programa analiza una oración ingresada por el usuario para proporcionar estadísticas sobre las palabras que contiene. 
      Primero, valida que la oración no esté vacía y que contenga al menos una palabra válida. Luego, separa las palabras y calcula 
      el número total de palabras, la primera y última palabra, así como la palabra más corta y la más larga. Finalmente, muestra estos 
      datos al usuario.

   - Inputs:
      - sentence.- String ingresado por el usuario.

   - Outputs:
      - "Word count: <n>"
      - "First word: <...>"
      - "Last word: <...>"
      - "Shortest word: <...>"
      - "Largest word: <...>"
      - "Error: you didn´t type a sentence"
      - "Error: invalid word"

   - Validations:
      - if sentence == "":
   print("Error: you didn´t type a sentence") .- Sucede cuando no se ingresa ninguna oración.
      - if len(separate_words) == 0:
      print("Error: invalid word") .- Debe haber al menos una palabra válida en la oración.

  
   - Test Cases: 
      # CASO NORMAL

      Type a sentence: The sun is bright
      Word count:  4
      First word:  The
      Last word:  bright
      Shortest word:  is
      Largest word:  bright

      
      # CASO BORDE

      Type a sentence: Hello
      Word count:  1
      First word:  Hello
      Last word:  Hello
      Shortest word:  Hello
      Largest word:  Hello


      # CASO ERROR

      Type a sentence: ""
      Error: you didn´t type a sentence

"""
print("\n")
print("----------------------------------PROBLEM-#4--------------------------------------------------------------------")

sentence= input("Type a sentence: ")
sentence= sentence.strip()
if sentence == "":
   print("Error: you didn´t type a sentence")
else:
   separate_words= sentence.split()
   if len(separate_words) == 0:
      print("Error: invalid word")
   else:
      word_count= len(separate_words)
      first_word= separate_words[0]
      last_word= separate_words[-1]
      shortest_word= separate_words[0]
      largest_word= separate_words[0]

      for word in separate_words:
         if len(word) < len(shortest_word):
            shortest_word= word
         if len(word) > len(largest_word):
            largest_word= word
      
      print("Word count: ", word_count)
      print("First word: ", first_word)
      print("Last word: ", last_word)
      print("Shortest word: ", shortest_word)
      print("Largest word: ", largest_word)

"""
# Problem 5: Password strength classifier

   - Descripción: 
      Este programa evalúa la fortaleza de una contraseña ingresada por el usuario. Primero, verifica que la contraseña no esté vacía. 
      Luego, analiza la contraseña para determinar si contiene letras mayúsculas, minúsculas, dígitos y símbolos especiales.     

   - Inputs:
      password: lo que el usuario escribe en el input("Type your password: ")

   - Outputs:
      "Error: didn´t type a password"
      "Password strenght: WEAK"
      "Password strenght: STRONG"
      "Password strenght: MEDIUM"

   - Validations:
      - if password == "": .- Verifica que el usuario haya ingresado una contraseña.

   - Test Cases: 
      # CASO NORMAL

      Type your password: Charly212!
      Password strenght: STRONG

      
      # CASO BORDE

      Type your password: Hola1234
      Password strenght: MEDIUM


      # CASO ERROR

      Type your password: ""
      Error: didn´t type a password

"""
print("\n")
print("-----------------------PROBLEM-#5-------------------------------------------------------------------------------")

password= input("Type your password: ")
if password == "":
   print("Error: didn´t type a password")
else:
   has_upper= False
   has_lower= False
   has_symbol= False
   has_digit= False

   for character in password:
      if character.isupper():
         has_upper= True
      elif character.islower():
         has_lower= True
      elif character.isdigit():
         has_digit= True
      elif not character.isalnum():
         has_symbol= True

   if len(password) < 8:
      print("Password strenght: WEAK")
   elif has_upper and has_lower and has_digit and has_symbol:
      print("Password strenght: STRONG")
   else:
      print("Password strenght: MEDIUM")

"""
# Problem 6: Product label formatter (fixed-width text)

   - Descripción: 
      Este programa genera una etiqueta de producto con un formato específico. 
      Solicita al usuario que ingrese el nombre del producto y su precio. 
      Luego, valida que el nombre no esté vacío y que el precio sea un número positivo. 
      Si las entradas son válidas, crea una etiqueta que incluye el nombre y el precio del producto, 
      asegurándose de que la etiqueta tenga exactamente 30 caracteres de ancho, truncando o rellenando con espacios según sea necesario. 
      Finalmente, muestra la etiqueta formateada al usuario.

   - Inputs:
      - product_name = ingresado por el usuario con input("Type the product name: ")
      - price_value = ingresado por el usuario con input("Type the product price: $")

   - Outputs:
      - print("Error: invalid product name") .- Mensaje de error si el nombre es inválido.
      - print("Error: invalid price value") .- Mensaje de error si el precio no es válido (no numérico o no positivo).
      - print("Label:", "" + label + "") .- Muestra la etiqueta formateada si las entradas son válidas.

   - Validations:
      - product_name == "" .- Error si está vacío tras strip().
      - price_value .- Convertible a float usando try/except.
  
   - Test Cases: 
      # CASO NORMAL

      Type the product name: Apples
      Type the product price: $12.5
      Label: Product: Apples Price: 12.5

      
      # CASO BORDE

      Type the product name: ExtraLargeWatermelonFruit
      Type the product price: $10
      Label: Product ExtraLargeWatermel


      # CASO ERROR

      Type the product name: "  "
      Type the product price: $abc
      Error: invalid product name
"""

print("\n --------------------------PROBLEM-#6----------------------------------------------------------------------------")

product_name= input("Type the product name: ")  
product_name= product_name.strip()
price_value= input("Type the product price: $")
if product_name == "":
   print("Error: invalid product name")
else:
   try:
      price_num= float(price_value)
      if price_num <= 0:
         print("Error: invalid price value")
      else:
         label= "Product " + product_name + " Price: " + str(price_num)
         if len(label) > 30:
            label= label[:30]
         while len(label) < 30:
            label = label + " "
         print("Label:", "" + label + "")
   except:
      print("Error: invalid price value")

print("---------------------------------END----------------------------------------------------------------------------")

# CONCLUSIONES
"""
   - El manejo adecuado de strings en Python es esencial para procesar y validar datos de entrada de manera efectiva.
   - La validación y normalización de datos ayuda a garantizar la integridad y seguridad de la información en aplicaciones.   
   - Aplicar buenas prácticas de codificación mejora la legibilidad y mantenibilidad del código.
   - La comprensión de los métodos de string y su uso adecuado facilita la manipulación de texto               
      en diversas situaciones, desde la validación de correos electrónicos hasta la generación de etiquetas de productos.
   
"""

# REFERENCIAS
"""
   - Documentación oficial de Python sobre strings: https://docs.python.org/3/library/stdtypes.html#str
   - Tutoriales de manejo de strings en Python: https://realpython.com/python-strings
   - Artículos sobre validación y normalización de datos: https://towardsdatascience.com/data-validation-and-cleaning-in-python-5f1f2d3f4f8e
   - Buenas prácticas de codificación en Python: https://peps.python.org/pep-0008/
   - Recursos sobre seguridad de contraseñas: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

"""
#REPOSITORIO DE GITHUB
"""
https://github.com/davidgerardoperez525/U2_CHARLY_HOMEWORK.git


"""