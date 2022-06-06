def leer_archivo(nombre):
    archivo = open(nombre,"rt", encoding=('utf8'))
    contenido = archivo.read()
    return contenido
def menu():
    print("Datos Producto")
    print("1. Listar")
    print("2. Agregar")
    print("3. Salir")
opciones=["Listar","Agregar","Salir"]

veces=0
while True:    
    usu=str(input("usuario: "))
    cont=int(input("pass: "))
    if usu==str(leer_archivo('usuario.txt').strip()) and cont==int(leer_archivo('claves.txt').strip()):
        break
    veces+=1
    if veces==3:
        print("demasiados intentos")
        break
if veces<3:
    menu()
    op=int(input("elija opcion: "))
    print(opciones[op-1])