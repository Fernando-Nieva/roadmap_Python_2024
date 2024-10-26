
#* Funciones simples
def my_funcion_Basica():
    print("Esto es una funcion basica")

def my_funcion_con_retorno():
    return "Esto es una funcion con retorno"

my_funcion_Basica()
retorno=my_funcion_con_retorno()
print(retorno)

print("\n")
#* Funciones con Argumento 

def my_funcion_con_Parametro( parametro1):
    numero = parametro1
    print(f"Esto es una función con 1 parámetros:{numero}")

def my_funcion_con_Parametros( parametro1, parametro2):
    numero = parametro1
    numero2 = parametro2
    print(f"Esto es una función con 2 parámetros:{numero} {numero2}")

my_funcion_con_Parametro("hola")
my_funcion_con_Parametros("hola","Fernando")

print("\n")
#* Funciones con Argumento predeterminado


def my_funcion_predeterminada( name="Usuario"):
    nombre = name
    print(f"Bienvenido:{nombre}")

my_funcion_predeterminada()

print("\n")
#* Funciones con Argumento y retorno

def my_funcion_ArgRet( saludo,nombre):
    return f"{saludo},{nombre}"

print(my_funcion_ArgRet("Hola","Fernando"))

print("\n")
#* Funciones con retorno de varios valores

def my_retornos():
    return "id:554854","usuario:opentalk"
# Desempaquetar los valores retornados en dos variables
valor1, valor2 = my_retornos()

print(valor1)
print(valor2)

print("\n")
#* Con un número variable de argumentos

def varios_argumentos(*argumentos):
        for argumento in argumentos:
            print(f"Bienvenido {argumento}!")

varios_argumentos("fernanado","Camilo","Juan","Maria")

print("\n")
#* Con un número variable de argumentos y con palabra clave

def registrar_usuario(**user):
    print("Registrando la siguiente información del usuario:")
    
    # user es un diccionario, así que usamos .items() para obtener clave y valor
    for clave, valor in user.items():
        print(f"{clave.capitalize()}: {valor}")

# Llamar a la función pasando múltiples argumentos con palabras clave
registrar_usuario(
    nombre="Fernando",
    edad=32, 
    ciudad="Buenos Aires", 
    profesion="Ilustrador")


print("\n")
# * Funciones dentro de funciones

def my_funcion_con_funciones():
     def funcion_numero1():
        print("funcion interna1")
     def funcion_numero2():
        print("funcion interna2")
     funcion_numero1()   
     funcion_numero2()   
     
my_funcion_con_funciones()



print("\n")
# * Funciones del lenguaje(built-in)


print(len("FERNANDO"))
print(type("FERNANO"))
print("Fernando Nieva".upper())



print("\n")
# * variables Locales y Globales

# Variable global
mensaje = "Esta es una variable global"

def mostrar_mensajes():
    # Variable local
    mensaje = "Esta es una  variable local"
    print(mensaje)  # Imprime el mensaje local
# Llamamos a la función que usa la variable local
mostrar_mensajes()
# Imprimimos la variable global
print(mensaje)


print("\n")
# * Extra


def my_funcion_extra(parametro1, parametro2):
    count = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(parametro1 + " y " + parametro2)  # Múltiplo de 3 y 5
        elif numero % 3 == 0:
            print(parametro1)  # Múltiplo de 3
        elif numero % 5 == 0:
            print(parametro2)  # Múltiplo de 5
        else:
            print(f"Número: {numero}")  # Ninguno de los anteriores
            count +=1
    return count
# Llamada a la función con los valores deseados
print(my_funcion_extra("multiplo de 3", "multiplo de 5"))