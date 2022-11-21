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
