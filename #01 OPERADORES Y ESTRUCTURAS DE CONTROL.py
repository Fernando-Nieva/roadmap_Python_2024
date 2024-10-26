
# operadores Aritméticos
a=10
b=10
print(f"suma: {a} + {b} =",(a+b))
print(f"resta: {a} - {b} =",(a-b))
print(f"multiplicacion: {a} * {b} =",(a*b))
print(f"divicion: {a} / {b} =",(a/b))
print(f"módulo: {a} % {b} =",(a%b))
print(f"exponente: {a} ** {b} =",(a**b))
print(f"divicion entera: {a} % {b} =",(a//b))

print("\n")
# operadores de  Comparación:
print(f"igualacion:{a} = {b} =",(a==b))
print(f"Distinto {a} de {b} =",(a!=b))
print(f"{a} mayor que {b} =",(a>b))
print(f"{a} menor que {b} =",(a<b))
print(f"{a} mayor igual que {b} =",(a>=b))
print(f"{a} menor igual que {b} =",(a<=b))


print("\n")
# operadores de  Lógicos:

x = True
y = False

print( f"AND && retorna true si entre ({x},{y}) ambas son verdaderas:",(x and y))  # False
print( f"OR || retorna true si entre ({x},{y}) una es verdaderas:",(x or y))  # False
print( f"NOT ! niega el valor  de ({x}) :",( not x))  # False


print("\n")
#  Operadores de Asignación:
my_number=25
print (f"Asignación simple :",(my_number))
my_number +=4
print (f"Asignación con suma :",(my_number))
my_number -=4
print (f"Asignación con resta :",(my_number))
my_number *=4
print (f"Asignación con multiplicacion :",(my_number))
my_number /=4
print (f"Asignación con división :",(my_number))
my_number %=4
print (f"Asignación con módulo :",(my_number))
my_number //=4
print (f"Asignación con divicion entera :",(my_number))
my_number **=4
print (f"Asignación con exponente :",(my_number))


print("\n")
# Operadores de Identidad:
variable_1 = [1, 2, 3]
variable_2 = variable_1
variable_3 = [1, 2, 3]
print(f"variable_1 y variable2 apuntan al mismo objeto:",(variable_1 is variable_2))  # True
print(f"variable_1 y variable3 apuntan al mismo objeto:",(variable_1 is variable_3))  # True
print(f"variable_1 y variable3 apuntan a objetos diferentes:",(variable_1 is not variable_3))  # True


print("\n")
#  Operadores de Pertenencia:

lista = [1, 2, 3, 4]
print("3 in lista:",(3 in lista))  # True
print("5 in lista",(5 in lista))  # false
print("5 not in lista",(5 not in lista))  # True

print("\n")

# Operadores a Nivel de Bits:

x = 5  # 101 en binario
y = 3  # 011 en binario

print(f"AND: {x} &  {y}:",(x & y))  #1(001 en binario)
print(f"OR:  {x} |  {y}:",(x | y))  #7(111 en binario)
print(f"XOR: {x} ^  {y}:",(x ^ y))  #6(011 en binario)
print(f"NOT: ~ {x} :",( ~ x)) 
print(f"Desplazamiento ala derecha   : {x} >>  {y}:",(x >> y))  #0(000 en binario)
print(f"Desplazamiento ala izquierda : {x} << {y}:",(x << y))  #40(101000 en binario)

print("\n")


'''Estructura de control'''

# Condicionales

# my_string="God of war"
my_string="tekken6"

if my_string == "God of war":
    print("Si ese juego existe en el catalogo")
elif my_string =="tekken6":
        print("si es un juego de lucha del catalgo")    
else:
    print("No ese juego no existe en nuestro catalogo")

print("\n")

# Interativas 

# Imprimir todas las letras del abecedario en minúsculas una al lado de la otra
for letra in range(ord('a'), ord('z') + 1):
    print(chr(letra), end=' -')

print("\n")

my_abc = ord('a') # Comenzar desde 'a' (valor ASCII 97)
while my_abc <= ord('z'): 
    print(chr(my_abc), end=' ')  
    my_abc += 1  # Incrementar la variable para pasar a la siguiente letra

print("\n")

# Manejo de excepciones (try, except, finally)

try:
    numero = int(input("Introduce un número: "))
    print(f"El número que introdujiste es: {numero}")
except:
    print("Error: No introdujiste un número válido.")
finally:
    print("finalizo él manejo de excepciness.")

print("\n")



#  * DIFICULTAD EXTRA (opcional):

for numero in range(10, 56):
    if numero % 2 == 0 and numero != 16 and numero % 3!=0:
        print((numero), end=' ')
print("\n")