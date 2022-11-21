C=[]
contraseñas=[]
usuarios=[]

import re
from string import punctuation
#Lista de Clientes
class Clientes(object):
    def __init__(self, nombre, apellido,tel,correo,contraseña, ):
        self.nombre = nombre
        self.apellido = apellido
        self.tel = tel
        self.correo = correo
        self.contraseña = contraseña
def Registrar():
    print("Inicio del Registro\n")
    while True:
        try:
            nombre = input("Ingrese su nombre: ")
            if len(nombre.strip()) != 0:
                break
        except:
            pass
    while True:
        try:
            apellido = input("Ingrese su apellido: ")
            if len(apellido.strip()) != 0:
                break
        except:
            pass
    while True:
        tel = input("Ingrese su teléfono: ")
        if len(tel) != 9 or len(tel.strip())==0:
             print("Ingrese un número de teléfono válido")
             pass
        else:
            break
    while True:
        correo = input("Ingrese un correo: ")
        if es_correo_valido(correo):
            print("Correo válido")
            break
        else:
            print("El correo no es válido")

    while True:
        intentos = 0
        contraseña = input("Introduce contraseña: ")
        intentos += 1
        if validador_contraseña(contraseña):
            print("La contraseña introducida ha sido {}".format(contraseña))
            break
        elif intentos > 5:
            contraseña = None
            print("No ha sido posible establecer una contraseña")
            break
    ObjCliente = Clientes(nombre,apellido,tel,correo,contraseña)
    C.append(ObjCliente)
    contraseñas.append(contraseña)
    usuarios.append(correo)
def validador_contraseña (cts):
    if len (cts) < 6 or len (cts) > 12:
        print ("La contraseña ha de tener entre 6 y 12 carácteres")
    elif not any ([c.isdigit() for c in cts]):
        print ("La contraseña ha de contener algún dígito")
    elif not any ([c.islower () for c in cts]):
        print ("La contraseña ha de contener alguna minúscula")
    elif not any ([c.isupper () for c in cts]):
        print ("La contraseña ha de contener alguna mayúscula")
    elif not any ([True if C in punctuation else False for C in cts]):
        print ("La contraseña ha de contener algún carácter especial")
    else:
        return True
    return False
def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

def contraseña_existente(contra):
  if contra in contraseñas:
      print("Bienvenido")
  else:
      print("Contraseña incorrecta")
def correo_existente(usuario):
    if usuario in usuarios:
        print("Usuario Correcto")
    else:
        print("El usuario no existe")

class Propiedad:
    def __init__(self, codigo, ubicacion, precio):
        self.__codigo = codigo
        self.__ubicacion = ubicacion
        self.__precio = precio
    def actualizarDatos(self):
        clave = input("Ingrese la clave: ")
        if clave == "2111":
            while True:
                print("Qué desea actualizar: ")
                print("1. Código: ", self.__codigo)
                print("2. Ubicación: ", self.__ubicacion)
                print("3. Precio: ", self.__precio)
                print("4. Salir")
                opc = input("Seleccione una opción: ")
                if opc == "4":
                    break
                elif opc == "1":
                    while True:
                        try:
                            codigo = input("Ingrese el nuevo Código: ")
                            int(codigo)
                            if len(codigo) == 8:
                                self.__codigo = codigo
                                break
                        except:
                            pass
                elif opc == "2":
                    ubicacion = input("Ingrese la nueva ubicacion: ")
                    self.__ubicacion = ubicacion
                elif opc == "3":
                    precio = float(input("Ingrese el nuevo precio: "))
                    self.__precio = precio
                else:
                    print("Opción equivocada")
        else:
            print("No autorizado para actualizar datos")
    def getCodigo(self):
        return self.__codigo
    def setCodigo(self, codigo):
        self.__codigo = codigo
    def getUbicacion(self):
        return self.__ubicacion
    def getPrecio(self):
        return self.__precio
# Funciones del p.principal
def ingresar():
    print(" ** Ingresando una nueva propiedad ** ")
    while True:
        codigo = input("Ingrese Código: ")
        if codigo not in COD and len(codigo) == 8:
            break
    while True:
        ubicacion = input("Ingrese la ubicación: ")
        if len(ubicacion) >= 3:
            break
    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio > 1000:
                break
        except:
            pass

    objeto = Propiedad(codigo, ubicacion, precio)
    COD.append(codigo)
    L.append(objeto)
def eliminar():
    print("Ingrese el código de la propiedad a eliminar")
    codigo = input("Ingrese el Código: ")
    try:
        ind = COD.index(codigo)
        del COD[ind]
        del L[ind]
        print("Se elimino la propiedad")
    except:
        print("El Código no existe: ")
def editar():
    print("Ingrese el código de la propiedad a editar")
    codigo = input("Ingrese el Código: ")
    try:
        ind = COD.index(codigo)
        codigoOriginal = L[ind].getCodigo()
        L[ind].actualizarDatos()
        COD[ind] = L[ind].getCodigo()
        if COD.count(COD[ind]) > 1:
            L[ind].setCodigo(dniOriginal)
            COD[ind] = codigoOriginal
    except:
        print("El Código no existe")
def visualizar():
    print("{0:12}{1:16}{2:>10}".format("Código", "Ubicación", "Precio"))
    for x in L:
        print("{0:12}{1:16}{2:10}".format(x.getCodigo(), x.getUbicacion(), x.getPrecio()))
def inversion():
    visualizar()
    INV = [x.getPrecio() for x in L]
    print("El precio total de todas las propiedades es: ", sum(INV))

# Programa principal
COD = []
L = []
while True:
    print("1. Ingresar una nueva propiedad")
    print("2. Eliminar una propiedad")
    print("3. Editar los datos de alguna propiedad")
    print("4. Visualizar todas las propiedades")
    print("5. Visualizar el precio acumulado de todas las propiedades")
    print("6. Salir")
    opc = input("Selecciones una opción: ")
    if opc=="6":
        break
    elif opc=="1":
        ingresar()
    elif opc=="2":
        eliminar()
    elif opc=="3":
        editar()
    elif opc=="4":
        visualizar()
    elif opc=="5":
        inversion()
