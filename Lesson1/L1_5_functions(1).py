""" Definición """

# args
def es_par(n1:int) -> bool:
    if n1%2 == 0:
        return True
    else:
        return False

# return None
def dar_bienvenida() -> None:
    nombre = input("Digite su nombre: ")
    edad = int(input("Digite su edad: "))
    print("Bienvenido " + nombre + ", su edad es " + str(edad) + ".")
    
# kwargs
def raiz(base:int, indice:int=2) -> float:
    root = base ** (1/indice)
    return root

""" Llamado """

num1 = 3
valor = es_par(num1)
print("¿El número " + str(num1) + " es par? -> " + str(valor))

dar_bienvenida()

num2 = 16
root2 = raiz(num2)
print("La raíz cuadrada de " + str(num2) + " es: " + str(root2))


root4 = raiz(num2, indice=4)
print("La raíz cuarta de " + str(num2) + " es: " + str(root4))
    


