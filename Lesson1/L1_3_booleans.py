""" Booleanos 

Solo pueden tomar 2 valores:
    True y False

"""

""" Operadores Lógicos """

# not
not False      #True
not True       #False

# or
True  or True  #True
True  or False #True
False or True  #True
False or False #False

# and
True  or True  #True
True  or False #False
False or True  #False
False or False #False

""" Operadores de comparación """
# < (Menor)
1  <   2   #True

# > (Mayor)
'a' > 'b'  #False

# >= (Mayor o Igual)
3  >=  3  #True

# <= (Menor o Igual)
3  <=  2  #False

# == (Igual)
3  ==  1  #False

# != (Diferente)
3  !=  4  #True
not (3  ==  4)

""" BLOQUE Condicional en cascada.
if - elif - else """

val1 = bool()
val2 = bool()
val3 = bool()


if val1:
    ...             # Si val1 == True
elif val2:
    ...             # Si (val1 == False) and (val2 == True)
elif val3:
    ...             # Si (val1 == False) and (val2 == False) and (val3 == True)
else:
    ...             # Si (val1 == False) and (val2 == False) and (val3 == False)

""" Operador Ternario """

name = input("Digite su nombre: ")
x = 0 if name == "Tony" else 1 # Si el nombre es "Tony", x=0 de lo contrario, x=1

""" Representación Numérica de Booleanos """

True   == 1 
False  == 0

False - True # 0 - 1 == -1

""" Operadores Identidad y Pertenencia """

# in (pertenencia)

'a' in "hola" # True
'k' in "hola" # False

# is (identidad)
x1 = 0
x2 = False

x1 == x2 # True (False == 0)
x1 is x2 # False
