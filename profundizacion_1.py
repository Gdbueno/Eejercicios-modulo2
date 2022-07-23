# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
#suma
print ('ingrese el primer numero a operar')
numero_1 = int (input())
print ('ingrese el segundo numero a operar')
numero_2 = int (input())
suma = numero_1 + numero_2
print ('el resultado de sumar', numero_1,'y', numero_2, 'es', suma)
#resta
resta = numero_1 - numero_2
print ('el resultado de restar', numero_1,'y', numero_2, 'es', resta)
#multiplicacion
multiplicacion = numero_1 * numero_2
print ('el resultado de multiplicar', numero_1,'y', numero_2, 'es', multiplicacion)
#division
division = numero_1 / numero_2
print ('el resultado de dividir', numero_1,'y', numero_2, 'es', division)
#exponente/potencia
exponente = numero_1 **2
print ('la potencia cuadrada de', numero_1,'es', exponente)
print ('fin de calculadora')
