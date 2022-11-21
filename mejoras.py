import re
from string import punctuation #Importar librería con carácteres especiales

class Clientes(object):
    def __init__(self,n,nombre, apellido,tel,correo,contraseña, ):
        self.__n = n
        self.__nombre = nombre
        self.__apellido = apellido
        self.__tel = tel
        self.__correo = correo
        self.__contraseña = contraseña
    def getContraseña(self):
     clave=input("Ingrese la clave: ")
     if clave in contraseñas:
         return self.__contraseña
     else:
         return "No esta autorizado para entrar a esta cuenta"
    def getNombre(self):
        return self.__nombre
    def getn(self):
        return self.__n
    def getApellido(self):
        return self.__apellido
    def getTel(self):
        return self.__tel
    def getCorreo(self):
        return self.__correo


class Propiedad:
    def __init__(self, codigo, ubicacion, precio, m2, estado, habitaciones, tipo):
        self.__codigo = codigo
        self.__ubicacion = ubicacion
        self.__precio = precio
        self.__m2 = m2
        self.__estado = estado
        self.__habitaciones = habitaciones
        self.__tipo = tipo

    def actualizarDatos(self):
        clave = input("Ingrese la clave: ")
        if clave == "2111":
            while True:
                print("Qué desea actualizar: ")
                print("1. Código: ", self.__codigo)
                print("2. Ubicación: ", self.__ubicacion)
                print("3. Precio: ", self.__precio)
                print("4. M2: ", self.__m2)
                print("5. Estado de la obra: ", self.__estado)
                print("6. N° de habitaciones: ", self.__habitaciones)
                print("7. Tipo de vivienda: ", self.__tipo)
                print("8. Salir")
                opc = input("Seleccione una opción: ")
                if opc == "8":
                    break
                elif opc == "1":
                    while True:
                        try:
                            codigo = input("Ingrese el nuevo Código: ")
                            int(codigo)
                            if len(codigo) == 4:
                                self.__codigo = codigo
                                break
                        except:
                            pass
                elif opc == "2":
                    ubicacion = input("Ingrese la nueva ubicacion: ")
                    self.__ubicacion = ubicacion
                elif opc == "3":
                    precio = int(input("Ingrese el nuevo precio: "))
                    self.__precio = precio
                elif opc == "4":
                    m2 = int((input("Ingrese el área corregida: ")))
                    self.__m2 = m2
                elif opc == "5":
                    estado = (input("Ingrese el estado de la obra corregido: "))
                    self.__estado = estado
                elif opc == "6":
                    habitaciones = int(input("Ingrese el nuevo número de habitaciones: "))
                    self.__habitaciones = habitaciones
                elif opc == "7":
                    tipo = input("Ingrese el tipo de vivienda (Casa o Departamento): ")
                    self.__tipo = tipo
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
    def getM2(self):
        return self.__m2
    def getEstado(self):
        return self.__estado
    def getHabitaciones(self):
        return self.__habitaciones
    def getTipo(self):
        return self.__tipo


#Funciones del Programa

def ver_datos_cliente_contacto():
    while True:
     print("Buscar cliente\n")
     n = int(input("Ingrese el número del cliente: "))
     try:
           ind = Cont.index(n)
           x=C[ind]
           print(
            "{0:12}{1:16}{2:15}{3:14}{4:18}".format("N°", "Nombre", "Apellido", "Teléfono", "Correo"))
           print("{0:12}{1:16}{2:15}{3:14}{4:18}".format(str(x.getn()), x.getNombre(), str(x.getApellido()),

                                                      str(x.getTel()), x.getCorreo()))
           break
     except:
          print("El N° no existe")

def Registrar():
    print("Inicio del Registro\n")
    n=len(C)+1
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
        if len(tel) != 9 or len(tel.strip())==0 or tel[0]!="9":
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
    ObjCliente = Clientes(n,nombre,apellido,tel,correo,contraseña)
    C.append(ObjCliente)
    contraseñas.append(contraseña)
    usuarios.append(correo)
    Cont.append(n)

def visualizar_cliente():
    print(
            "{0:12}{1:16}{2:15}{3:14}{4:18}".format("N°", "Nombre", "Apellido", "Teléfono","Correo"))
    for x in C:
        print("{0:12}{1:16}{2:15}{3:14}{4:18}".format(str(x.getn()), x.getNombre(), str(x.getApellido()),

                                                             str(x.getTel()), x.getCorreo()))

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
      return True
  else:
      return False

def correo_existente(usuario):
    if usuario in usuarios:
        return True
    else:
        return False

def contactar():
    while True:
     print("Ingrese el código de la propiedad que desea adquirir: ")
     cod=input("Ingresa el código: ")
     try:
        ind = COD.index(cod)
        x=L[ind]
        print("{0:12}{1:16}{2:10}{3:10}{4:20}{5:15}".format("Código", "Ubicación", "Precio", "M2", "Estado de la obra",
                                                            "N° de Habitaciones"))
        print("{0:12}{1:16}{2:10}{3:10}{4:20}{5:15}".format(x.getCodigo(), x.getUbicacion(), str(x.getPrecio()),
                                                            str(x.getM2()), x.getEstado(), str(x.getHabitaciones())))
        print("Muy pronto nos pondremos en contacto con usted")
        break
     except:
        print("El Código no existe: ")

def ingresar():
    print(" ** Ingresando una nueva propiedad ** ")
    while True:
        codigo = input("Ingrese Código: ")
        if codigo not in COD and len(codigo) == 4:
            break
        else:
            print("Ingrese un código válido")
    while True:
        ubicacion = input("Ingrese la ubicación: ")
        if len(ubicacion) >= 3:
            break
        else:
            print("Ingrese una ubicación válida")
    while True:
        try:
            precio = int(input("Ingrese el precio: "))
            if precio > 1000:
                break
            else:
                print("Ingrese un precio válido")
        except:
            pass
    while True:
        try:
            m2 = int(input("Ingrese el Área de la propiedad: "))
            if m2 > 15:
                break
            else:
                print("Ingrese un área válida")
        except:
            pass
    while True:
        estado = input("Ingrese el estado de la obra: ")
        if len(estado) >= 3:
            break
        else:
            print("Ingrese un estado de la obra válido")
    while True:
        try:
            habitaciones = int(input("Ingrese el N° de Habitaciones: "))
            if habitaciones >= 1:
                break
            else:
                print("Ingrese un N° de habitaciones válido")
        except:
            pass
    while True:
        tipo = input("Ingrese el tipo de vivienda (Casa o Departamento): ")
        if tipo.lower() == "casa" or tipo.lower() == "departamento":
            break
        else:
            print("Ingrese un tipo de vienda válido")
    objeto = Propiedad(codigo, ubicacion, precio, m2, estado, habitaciones, tipo)
    COD.append(codigo)
    L.append(objeto)

def ingresarauto():
    for x in range(len(L1)):
        codigo = L1[x][0]
        ubicacion = L1[x][1]
        precio = L1[x][2]
        m2 = L1[x][3]
        estado = L1[x][4]
        habitaciones = L1[x][5]
        tipo = L1[x][6]
        objeto = Propiedad(codigo, ubicacion, precio, m2, estado, habitaciones, tipo)
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
            L[ind].setCodigo(codigoOriginal)
            COD[ind] = codigoOriginal
    except:
        print("El Código no existe")

def visualizar():
    print("{0:12}{1:16}{2:10}{3:10}{4:20}{5:20}{6:25}".format("Código", "Ubicación", "Precio", "M2", "Estado de la obra", "N° de Habitaciones", "Tipo de vivienda"))
    for x in L:
        print("{0:12}{1:16}{2:10}{3:10}{4:20}{5:20}{6:25}".format(x.getCodigo(), x.getUbicacion(), str(x.getPrecio()), str(x.getM2()), x.getEstado(), str(x.getHabitaciones()), x.getTipo()))



def clientes():
  while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opc=input("Ingrese una opción: ")
    if opc=="1":
        Registrar()
        print("Registro Exitoso")
    if opc=="2":
        while True:
            correo = input("Ingrese su correo: ")
            if correo_existente(correo) == True:
                print("Correo Correcto")
                break
            else:
                print("No existe ese usuario")

        while True:
            contraseña=input("Ingrese su contraseña: ")
            if contraseña_existente(contraseña)==True:
                print("Bienvenido")
                break
            else:
                print("Contraseña incorrecta")
        while True:
            print("¿Qué desea hacer?")
            print("1. Ver productos")
            print("2. Contactar a un asesor")
            print("3. Salir")
            x=int(input("Elije una opción: "))
            if x==1:
                visualizar()
            elif x==2:
                contactar()
            elif x==3:
                break
    if opc=="3":
     break

def vendedor():
    while True:
        print("1. Ingresar una nueva propiedad")
        print("2. Eliminar una propiedad")
        print("3. Editar los datos de alguna propiedad")
        print("4. Visualizar todas las propiedades")
        print("5. Visualizar los clientes registrados en la plataforma")
        print("6. Buscar datos de los clientes que necesitan asesor")
        print("7. Salir")
        opc = input("Selecciones una opción: ")
        if opc == "7":
            break
        elif opc == "1":
            ingresar()
        elif opc == "2":
            eliminar()
        elif opc == "3":
            editar()
        elif opc == "4":
            visualizar()
        elif opc=="5":
            visualizar_cliente()
        elif opc=="6":
            ver_datos_cliente_contacto()

# Programa principal

L1 = [
   ["0001","Lince",110000,80,"En construcción",2,"Departamento"],
   ["0002","Miraflores",180000,120,"En construcción",3,"Casa"],
   ["0003","Breña",105000,70,"Acabada",3,"Departamento"],
   ["0004","San Miguel",106000,60,"En construcción",4,"Departamento"],
   ["0005","Surco",190000,70,"En construcción",3,"Departamento"],
   ["0006","Lince",100000,80,"Acabada",4,"Departamento"],
   ["0007","Miraflores",200000,67,"En construcción",5,"Departamento"],
   ["0008","San Isidro",250000,80,"Acabada",6,"Departamento"],
   ["0009","La Molina",300000,110,"En construcción",3,"Casa"],
   ["0010","Jesús María",110000,90,"Acabada",5,"Departamento"],
   ["0011", "Breña", 190000, 180, "Acabada", 5, "Casa"],
   ["0012", "Miraflores", 380000, 220, "Acabada", 6, "Casa"],
   ["0013", "Breña", 189000, 170, "Acabada", 5, "Casa"],
   ["0014", "Surco", 196000, 260, "Acabada", 6, "Casa"],
   ["0015", "Surco", 290000, 170, "Acabada", 5, "Casa"],
   ["0016", "Barranco", 190000, 280, "Acabada", 7, "Casa"],
   ["0017", "Miraflores", 200000, 167, "Acabada", 8, "Departamento"],
   ["0018", "San Isidro", 250000, 180, "Acabada", 5, "Departamento"],
   ["0019", "La Molina", 400000, 240, "Acabada", 6, "Casa"],
   ["0020", "Jesús María", 110000, 190, "Acabada", 5, "Departamento"]
   ]
L = []
COD = []
C=[]
Cont=[]
ingresarauto()
contraseñas=[]#Contraseñas de los clientes registrados
usuarios=[]#Usuarios de los clientes registrados

while True:
    print("\n")
    print("|****************************|")
    print("|**|  Maze Constructor    |**|")
    print("|**|         Menu         |**|")
    print("|****************************|")
    print("")
    print("1. Clientes")
    print("2. Vendedor")
    print("3. Salir")
    x=input("Ingrese una opción: ")
    if x=="1":
        clientes()
    elif x=="2":
        vendedor()
    elif x=="3":
        break
